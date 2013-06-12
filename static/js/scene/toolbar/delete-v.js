define([
	'backbone',
	'jquery'
], function(Backbone, $) {
    
	var DeleteView = Backbone.View.extend({
		tmpl: $('#delete-tmpl').html(),
		
		initialize: function() {
			this.$el.html(this.tmpl);
		},
		
		reset: function(step2) {
			this.$('.intent').toggle(!step2);
			this.$('.confirm').toggle(step2);
		},
		
		events: {
			'click .delete-intent': 'onIntent',
			'click .delete-cancel': 'onCancel',
			'click .delete-confirm': 'onConfirm'
		},
		
		onIntent: function() {
			this.reset(true);
		},
		
		onCancel: function() {
			this.reset();
		},
		
		onConfirm: function() {
			this.model.cancel();
			this.model.destroy();
		}
	});
	
	return DeleteView;
});