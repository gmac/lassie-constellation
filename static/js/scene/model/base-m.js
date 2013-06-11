define([
    'backbone',
    'jquery'
], function(Backbone, $) {
    
	var SCENE_ID = $('#scene-id').val();
	
	var SelectedModel = Backbone.Model.extend({
		model: null,
		
		api: function() {
			return this.model ? this.model.collection.api : '';
		},
		
		load: function(model) {
			if (this.model) {
				this.stopListening(this.model);
			}
			
			this.model = model;
			
			if (this.model) {
				this.listenTo(this.model, 'all', this.proxyEvent);
				this.listenTo(this.model, 'delete', this.unload);
				this.trigger('select');
			}
		},
		
		unload: function() {
			this.load(null);
		},

		proxyEvent: function(eventName) {
			this.trigger(eventName);
		},
		
		edit: function() {
			this.trigger('edit', this.api());
		},
		
		cancel: function() {
			this.trigger('cancel', this.api());
		},
		
		attrs: function() {
			return this.model ? this.model.attributes : this.attributes;
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
	});
	
	
	var SceneModelList = Backbone.Collection.extend({
		api: '',
		model: Backbone.Model,
		
		SILENT: {silent: true},
		SILENT_PATCH: {patch:true, silent: true},
		
		initialize: function() {
			this.selected = new SelectedModel();
		},
		
		url: function() {
			return '/api/v1/'+ this.api +'/';
		},
		
		sceneUrl: function() {
			return '/api/v1/scene/'+ SCENE_ID +'/';
		},
		
		getNewSlug: function() {
			if (!this.model) return 'new_object';
			
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
		
		getNewModel: function() {
			return {
				slug: this.getNewSlug(),
				scene: this.sceneUrl()
			};
		},
		
		create: function() {
			var data = this.getNewModel();
			Backbone.Collection.prototype.create.call(this, data);
			return this.where(data);
		},
		
		sync: function(method, model, options) {
			options.data = options.data || {};
			options.data.scene__id = SCENE_ID;
			options.data.format = 'json';
			Backbone.sync(method, model, options);
		},
		
		parse: function(data) {
			return data.objects;
		},
		
		comparator: function(model) {
			return model.get('slug');
		},
		
		select: function(model, edit) {
			if (model && typeof model !== 'object') {
				model = this.get(model);
			}

			this.selected.load(model);
			edit && this.selected.edit();
		}
	});
	
	SceneModelList.SCENE_ID = SCENE_ID;
	
	return SceneModelList;
});