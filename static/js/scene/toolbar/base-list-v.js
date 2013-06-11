define([
	'backbone'
], function(Backbone) {
    
	var BaseListView = Backbone.View.extend({
		
		setModel: function(model) {
			this.model = model;
			this.listenTo(this.model, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			this.model.each(function(model) {
				html += '<option value="'+ model.cid +'">'+ model.get('slug') +'</option>';
			});
			this.$('.list').html(html);
		},
		
		events: {
			'change .list': 'onSelect',
			'click .add': 'onAdd',
			'click .edit': 'onEdit'
		},
		
		getValue: function() {
			return this.$('.list').val();
		},
		
		onSelect: function() {
			this.model.select(this.getValue());
		},
		
		onAdd: function() {
			this.model.create();
		},
		
		onEdit: function() {
			this.model.select(this.getValue(), true);
		}
	});

	return BaseListView;
});