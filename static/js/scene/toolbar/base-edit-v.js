define([
	'backbone'
], function(Backbone) {
    
	var deleteTmpl = $('#model-delete-tmpl').html();

	var BaseEditView = Backbone.View.extend({
		
		initialize: function() {
			if (!this.collection) throw('Edit view requires a resource collection.');
			
			// Set selection proxy as the view model:
			this.model = this.collection.selected;
			this.listenTo(this.model, 'select change', this.populate);
			
			// Populate component layouts:
			this.$delete = this.$('.model-delete').html(deleteTmpl);
			
			// Run custom setup:
			this.setup();
		},
		
		setup: function() {
			// override...
		},
		
		// Populates all attribute fields:
		populate: function() {
			_.each(this.model.attrs(), function(value, attribute) {
				this.$('[name="'+attribute+'"]').val(value);
			}, this);
		},
		
		// Toggles the delete form state:
		toggleDelete: function(step2) {
			this.$delete.find('.intent').toggle(!step2);
			this.$delete.find('.confirm').toggle(step2);
		},
		
		events: {
			'click .cancel-edit': 'onCancel',
			'click .delete': 'onDelete'
		},
		
		onCancel: function() {
			this.model.cancel();
		},
		
		onDelete: function(evt) {
			var op = $(evt.currentTarget).attr('data-op');
			switch (op) {
				case 'intent': this.toggleDelete(true); return;
				case 'cancel': this.toggleDelete(false); return;
			}
			this.toggleDelete(false);
			this.model.cancel();
			this.model.destroy();
		}
	});

	return BaseEditView;
});