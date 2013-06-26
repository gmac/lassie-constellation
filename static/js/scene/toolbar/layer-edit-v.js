define([
	'underscore',
	'common/base-edit-v',
	'../model/layer-m'
], function(_, BaseEditView, layersResource) {

	var LayerEditView = BaseEditView.extend({
		el: '#layer-edit',
		
		events: function() {
			return _.extend({
				'click .actions-edit': 'onActions'
			}, BaseEditView.prototype.events);
		},
		
		onActions: function() {
			var resourceUri = this.model.get('resource_uri');
			
			require(['jquery_colorbox', 'action/main'], function($, actionsManager) {
				$.colorbox({
					inline: true,
					href: '#actions-edit',
					maxHeight: '90%'
				});
				
				actionsManager.load(resourceUri);
			});
		}
	});

	return new LayerEditView({
		collection: layersResource,
		model: layersResource.selected
	});
});