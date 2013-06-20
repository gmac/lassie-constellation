define([
	'underscore',
	'common/base-edit-v',
	'../model/layer-m'
], function(_, BaseEditView, layersResource) {

	var LayerEditView = BaseEditView.extend({
		el: '#layer-edit',
		
		events: function() {
			return _.extend({
				'click .edit-actions': 'onEditActions'
			}, BaseEditView.prototype.events);
		},
		
		onEditActions: function() {
			require([
				'jquery_colorbox',
				'interaction/main'
			], function($, actionsManager) {
				actionsManager.load(layersResource.selected.get('resource_uri'));
				$.colorbox({inline: true, href: '#layer-actions', maxHeight: '90%'});
			});
		}
	});

	return new LayerEditView({
		collection: layersResource,
		model: layersResource.selected
	});
});