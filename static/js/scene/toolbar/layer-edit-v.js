define([
	'underscore',
	'./base-edit-v',
	'../model/layer-m'
], function(_, BaseEditView, layersResource) {

	var LayerEditView = BaseEditView.extend({
		el: '#layer-edit',

		setup: function() {
			//this.listenTo(selectedModel, 'select change', this.render);
			//this.listenTo(selectedModel, 'change:float_enabled', this.renderSubtitle);
			//this.listenTo(selectedModel, 'change:subtitle_color', this.renderSubtitle);
		},
		
		events: function() {
			return _.extend({
				//'change .string': 'onString',
				//'change .integer': 'onInteger'
			}, BaseEditView.prototype.events);
		}
		
		/*
		onSlug: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			selectedModel.set(field, target.val(), layersModel.SILENT);
		},
		
		onString: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			selectedModel.save(field, target.val(), layersModel.SILENT_PATCH);
		},
		
		onInteger: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			var value = parseInt(target.val(), 10);
			selectedModel.save(field, isNaN(value) ? 0 : value, layersModel.SILENT_PATCH);
		}*/
	});

	return new LayerEditView({
		collection: layersResource
	});
});