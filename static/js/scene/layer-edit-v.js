define([
	'backbone',
    'jquery',
	'underscore',
	'./layer-m'
], function(Backbone, $, _, layersModel) {
	
	var silent = {silent: true};
	var patch = {patch:true, silent: true};
	
	var LayerEditView = Backbone.View.extend({
		el: '#layer-edit',

		initialize: function() {
			this.listenTo(layersModel, 'select', this.load);
		},
		
		load: function(model) {
			this.model && this.stopListening(this.model);
			this.listenTo(model, 'change', this.render);
			this.listenTo(model, 'change:float_enabled', this.renderSubtitle);
			this.listenTo(model, 'change:subtitle_color', this.renderSubtitle);
			this.model = model;
			this.render();
		},
		
		render: function() {
			_.each(this.model.attributes, function(value, attribute) {
				this.$('[name="'+attribute+'"]').val(value);
			}, this);
			
			this.renderSubtitle();
		},
		
		renderSubtitle: function() {
			
		},
		
		events: {
			'change .string': 'onString',
			'change .integer': 'onInteger'
		},
		
		onSlug: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			this.model.set(field, target.val(), silent);
		},
		
		onString: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			this.model.save(field, target.val(), patch);
		},
		
		onInteger: function(evt) {
			var target = $(evt.target);
			var field = target.attr('name');
			var value = parseInt(target.val(), 10);
			this.model.save(field, isNaN(value) ? 0 : value, patch);
		}
	});

	return new LayerEditView();
});