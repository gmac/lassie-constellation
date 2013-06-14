define([
	'backbone',
	'jquery'
], function(Backbone, $) {
    
	var tmpl = '<div class="intent"><label>Danger</label><br>';
	tmpl += '<button class="delete" data-op="intent">Delete</button></div>';
	tmpl += '<div class="confirm" style="display:none;"><label>Are you sure?</label><br>';
	tmpl += '<button class="delete" data-op="confirm">Delete</button>';
	tmpl += '<button class="delete" data-op="cancel">Cancel</button></div>';

	var DeleteView = Backbone.View.extend({
		initialize: function() {
			this.$el.html(tmpl);
		},
		
		confirm: function(confirm) {
			this.$('.intent').toggle(!confirm);
			this.$('.confirm').toggle(confirm);
		},
		
		events: {
			'click .delete': 'onDelete'
		},
		
		onDelete: function(evt) {
			switch ($(evt.currentTarget).attr('data-op')) {
				case 'intent': this.confirm(true); return;
				case 'cancel': this.confirm(false); return;
			}
			this.confirm(false);
			this.model.cancel();
			this.model.destroy();
		}
	});
	
	return DeleteView;
});