define([
	'backbone',
	'jquery'
], function(Backbone, $) {
	
	var PATCH = {patch:true};
	
	var BaseEditView = Backbone.View.extend({
		
		populate: function() {
			var model = this.model;
			this.$('input[name]').each(function() {
				this.value = model.get(this.name) || '';
			});
		},
		
		events: {
			'change .text-field': 'onText',
			'change .slug-field': 'onSlug',
			'change .integer-field': 'onInteger',
			'change .percent-field': 'onPercent'
		},
		
		onText: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = field.val();
			this.model.save(name, value, PATCH);
		},
		
		onSlug: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = field.val();
			this.model.save(name, value, PATCH);
		},
		
		onInteger: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = parseInt(field.val(), 10);
			if (isNaN(value)) field.val(this.model.get('name'));
			else this.model.save(name, value, PATCH);
		},
		
		onPercent: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = parseInt(field.val(), 10);
			var valid = Math.max(0, Math.min(value, 100));
			if (isNaN(value)) {
				field.val(this.model.get('name'));
				return;
			}
			
			if (value !== valid) field.val(valid);
			this.model.save(name, valid, PATCH);
		}
	});
	
	return BaseEditView;
});