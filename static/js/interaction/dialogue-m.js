define([
	'backbone',
	'underscore',
	'common/resource-m',
	'./action-m'
], function(Backbone, _, ResourceModelList, actionResource) {
	
	var DialogueModel = Backbone.Model.extend({
		defaults: {
			index: 0,
			notes: '',
			related_target: '',
			slug: '',
			sound: '',
			title: '',
			tone: ''
		}
	});
	
	var DialogueModelList = ResourceModelList.extend({
		api: 'dialogue',
		model: DialogueModel,
		voices: actionResource.voices,
		
		initialize: function() {
			ResourceModelList.prototype.initialize.apply(this, arguments);
			this.listenTo(actionResource.selected, 'select', this.reload);
			this.listenTo(this, 'destroy', this.resetOrder);
		},
		
		reload: function() {
			this.reset();
			if (actionResource.selected.get('id')) {
				this.fetch(this.RESET);
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
				voice: actionResource.voices.at(0).get('id'),
				index: this.length
			};
		},
		
		getRequestData: function(method) {
			return {
				action__id: actionResource.selected.get('id'),
				format: 'json',
				limit: 0
			};
		},
		
		resetOrder: function() {
			this.each(function(model, index) {
				model.set('index', index);
			});
			this.reorder();
		},
		
		reorder: function() {
			this.sort();
			this.patch(this.map(function(model) {
				return model.pick('resource_uri', 'index');
			}));
		}
	});
	
	return new DialogueModelList();
});