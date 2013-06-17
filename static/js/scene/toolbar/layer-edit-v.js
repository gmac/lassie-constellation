define([
	'underscore',
	'common/base-edit-v',
	'../model/layer-m'
], function(_, BaseEditView, layersResource) {

	var LayerEditView = BaseEditView.extend({
		el: '#layer-edit'
	});

	return new LayerEditView({
		collection: layersResource,
		model: layersResource.selected
	});
});