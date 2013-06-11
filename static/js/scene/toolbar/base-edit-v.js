define([
	'backbone'
], function(Backbone) {
    
	var BaseEditView = Backbone.View.extend({
		
		setModel: function(modelCollection) {
			this.model = modelCollection.selected;
			this.listenTo(this.model, 'select change', this.populate);
		},
		
		populate: function() {
			_.each(this.model.attrs(), function(value, attribute) {
				this.$('[name="'+attribute+'"]').val(value);
			}, this);
		},
		
		events: {
			'click .cancel': 'onCancel',
		},
		
		onCancel: function() {
			this.model.cancel();
		}
	});

	return BaseEditView;
});