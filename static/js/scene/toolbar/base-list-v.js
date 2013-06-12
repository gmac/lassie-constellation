define([
	'backbone'
], function(Backbone) {
    
	var BaseListView = Backbone.View.extend({
		initialize: function() {
			if (this.collection) {
				this.listenTo(this.collection, 'add remove reset sync', this.render);
				this.listenTo(this.collection.selected, 'select', this.updateSelection);
			} else {
				throw('Requires a resource collection model.');
			}	
		},
		
		render: function() {
			var html = '';
			
			// Render list options, including selection state:
			this.collection.each(function(model) {
				html += '<option value="'+ model.cid +'"';
				if (model.cid === this.collection.selected.cid) {
					html += ' selected="selected"';
				}
				html += '>'+ model.get('slug') +'</option>';
			}, this);
			
			this.$('.list').html(html);
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