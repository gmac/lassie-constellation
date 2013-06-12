define([
	'backbone',
	'underscore',
	'common/resource-m',
	'./action-m'
], function(Backbone, _, ResourceModelList, actionResource) {
	
	var DialogueModelList = ResourceModelList.extend({
		api: 'dialogue',
		
		initialize: function() {
			ResourceModelList.prototype.initialize.apply(this, arguments);
			this.listenTo(actionResource.selected, 'select', this.reload);
		},
		
		reload: function() {
			this.reset();
			if (actionResource.selected.get('id')) {
				this.fetch();
			}
		},
		
		comparator: function(model) {
			return model.get('index');
		},
		
		// Gets a base fieldset for new models:
		// may be overridden in sub-classes to extend fields.
		getNewModelData: function() {
			return {
				action: actionResource.selected.get('resource_uri'),
				index: this.length
			};
		},
		
		getRequestData: function(method) {
			return {
				action__id: actionResource.selected.get('id'),
				format: 'json',
				limit: 0
			};
		}
	});
	
	return new DialogueModelList();
});