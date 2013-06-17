define([
	'backbone'
], function(Backbone) {
    
	var BaseListView = Backbone.View.extend({
		initialize: function() {
			if (this.collection) {
				this.listenTo(this.collection, 'add remove reset sync', this.render);
				this.listenTo(this.collection.selected, 'change:slug', this.render);
				this.listenTo(this.collection.selected, 'select', this.updateSelection);
			}
		},
		
		render: function() {
			// Render list options, including selection state:
			this.$('.list').html(this.collection.reduce(function(memo, model) {
				memo += '<option value="'+ model.cid +'"';
				if (model.cid === this.collection.selected.cid) {
					memo += ' selected="selected"';
				}
				return memo += '>'+ model.get('slug') +'</option>';
			}, '', this));
		},
		
		updateSelection: function() {
			this.$('.list').val(this.collection.selected.cid);
		},
		
		events: {
			'change .list': 'onSelect',
			'click .add': 'onAdd',
			'click .edit': 'onEdit'
		},

		onSelect: function() {
			this.collection.select(this.$('.list').val());
		},
		
		onAdd: function() {
			this.collection.create();
		},
		
		onEdit: function() {
			this.collection.selected.edit();
		}
	});

	return BaseListView;
});