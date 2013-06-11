define([
	'backbone',
    'jquery',
	'underscore',
	'../model/layer-m'
], function(Backbone, $, _, layersModel) {
	
	var selectedModel = layersModel.selected;
	
	var LayerEditView = Backbone.View.extend({
		el: '#layer-edit',

		initialize: function() {
			this.listenTo(selectedModel, 'select change', this.render);
			this.listenTo(selectedModel, 'change:float_enabled', this.renderSubtitle);
			this.listenTo(selectedModel, 'change:subtitle_color', this.renderSubtitle);
		},
		
		render: function() {
			_.each(selectedModel.attrs(), function(value, attribute) {
				this.$('[name="'+attribute+'"]').val(value);
			}, this);
			
			this.renderSubtitle();
		},
		
		renderSubtitle: function() {
			
		},
		
		events: {
			'change .string': 'onString',
			'change .integer': 'onInteger',
			'click .cancel': 'onCancel'
		},
		
		onCancel: function() {
			selectedModel.cancel();
		},
		
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
		}
	});

	return new LayerEditView();
});