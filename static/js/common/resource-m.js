define([
	'backbone',
	'underscore'
], function(Backbone, _) {
	
	function SelectionProxy(api) {
		this.api = api;
	}
	
	_.extend(SelectionProxy.prototype, {
		id: '',
		cid: '',
		api: '',
		model: null,

		load: function(model, options) {
			if (model === this.model) return;
			
			// Clear previous model:
			if (this.model) {
				this.stopListening(this.model);
			}
			
			// Subscribe to new valid model:
			if (model) {
				this.listenTo(model, 'all', this.proxyEvent);
			}
			
			// Store new model and trigger selection change:
			this.model = model;
			this.id = model ? model.id : '';
			this.cid = model ? model.cid : '';
			if (!options || !options.silent) this.trigger('select');
		},
		
		unload: function() {
			this.load(null);
		},

		proxyEvent: function(eventName) {
			this.trigger(eventName, this.model);
		},
		
		edit: function() {
			this.trigger('edit', this.api);
		},
		
		cancel: function() {
			this.trigger('cancel', this.api);
		},
		
		attrs: function() {
			return this.model ? this.model.attributes : this.attributes;
		},
		
		changedAttributes: function() {
			return this.model ? this.model.changedAttributes.apply(this.model, arguments) : false;
		},
		
		get: function() {
			return this.model ? this.model.get.apply(this.model, arguments) : null;
		},
		
		set: function() {
			return this.model ? this.model.set.apply(this.model, arguments) : null;
		},
		
		save: function() {
			return this.model ? this.model.save.apply(this.model, arguments) : null;
		},
		
		destroy: function() {
			return this.model ? this.model.destroy.apply(this.model, arguments) : null;
		}
	}, Backbone.Events);
	
	
	var ResourceModelList = Backbone.Collection.extend({
		api: '',
		hasData: false,
		
		RESET: {reset: true},
		SILENT: {silent: true},
		PATCH: {patch: true},
		SILENT_PATCH: {patch:true, silent: true},
		
		constructor: function() {
			this.selected = new SelectionProxy(this.api);
			this.listenTo(this, 'reset destroy', this.onReset);
			Backbone.Collection.prototype.constructor.apply(this, arguments);
		},
		
		// Automatically select first model when the collection resets:
		onReset: function() {
			this.selectAt(0);
		},
		
		url: function() {
			return '/api/v1/'+ this.api +'/';
		},
		
		formatUri: function(api, id) {
			return '/api/v1/'+ api +'/'+ id +'/';
		},
		
		// Selects a new default slug name (ie: "apiname0"):
		// searches the collection for existing defaults, and auto-increments.
		getNewSlug: function() {
			var slug = this.api;
			var inc = 0;
			
			this.each(function(model) {
				var modelSlug = model.get('slug');
				if (modelSlug.indexOf(slug) === 0) {
					var modelInc = parseInt(modelSlug.slice(slug.length), 10);
					inc = Math.max(inc, isNaN(modelInc) ? inc : modelInc+1);
				}
			});
			
			return slug + inc;
		},
		
		// Gets a base fieldset for new models:
		// may be overridden in sub-classes to extend fields.
		getNewModelData: function() {
			return {};
		},
		
		getRequestData: function(method) {
			return {};
		},
		
		// Creates a new model with the base fieldset, then selects it:
		create: function(attr, opts) {
			attr = _.extend(this.getNewModelData(), attr || {});
			var model = Backbone.Collection.prototype.create.call(this, attr, opts);
			this.select(model);
		},
		
		sync: function(method, model, options) {
			options.data = options.data || {};
			_.extend(options.data, this.getRequestData(method));
			Backbone.sync(method, model, options);
		},
		
		parse: function(data) {
			this.hasData = true;
			return data.objects;
		},
		
		selectAt: function(model, edit) {
			model = this.at(model);
			this.selected.load(model);
			model && edit && this.selected.edit();
		},
		
		select: function(model, edit) {
			model = this.get(model);
			this.selected.load(model);
			model && edit && this.selected.edit();
		},
		
		reorder: function() {
			this.sort();
			this.patch(this.map(function(model) {
				return model.pick('resource_uri', 'index');
			}));
		},
		
		patch: function(patch) {
			this.sync('patch', this, {
				data: JSON.stringify({objects: patch, format: 'json'}),
				contentType: 'application/json'
			});
		}
	});
	
	return ResourceModelList;
});