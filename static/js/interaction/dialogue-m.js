define([
	'backbone',
	'underscore',
	'common/proxy-m',
	'./action-m'
], function(Backbone, _, ProxyModel, actionModel) {
	
	var DialogueModelList = Backbone.Collection.extend({
		url: '/api/v1/dialogue/',
		
		initialize: function() {
			this.selected = new ProxyModel();
			this.listenTo(actionModel.selected, 'select', this.reload);
		},
		
		reload: function() {
			this.reset();
			this.fetch();
		},
		
		// HACK: request objects based on resource ID.
		// This *should* be requesting based on resource URI,
		// however Tastypie (API) seems to have issues filtering generic foreign keys.
		// Instead we'll request on resource id with no results limit,
		// and then filter out the relevant resources client-side.
		sync: function(method, model, options) {
			options.data = options.data || {};
			
			var action = actionModel.selected.get('id');
			if (action) options.data.action__id = action;
			
			options.data.format = 'json';
			options.data.limit = 0;
			Backbone.sync(method, model, options);
		},
		
		parse: function(response) {
			return response.objects;
		},
		
		create: function() {
			Backbone.Collection.prototype.create.call(this, {
				action: actionModel.selected.get('resource_uri'),
				index: this.length
			});
		},
		
		comparator: function(model) {
			return model.get('index');
		},
		
		select: function(model) {
			if (_.isString(model)) model = this.at(model);
			else if (_.isNumber(model)) model = this.at(model);
			
			if (model instanceof Backbone.Model) {
				this.selected.load(model);
			}
		}
	});
	
	return new DialogueModelList();
});