define([
	'backbone',
	'jquery',
	'common/delete-v',
	'./action-m'
], function(Backbone, $, DeleteWidget, actionsModel) {
	
	var ActionsView = Backbone.View.extend({
		el: '#actions-manager',
		
		initialize: function() {
			this.listenTo(actionsModel, 'add remove reset sync', this.render);
			this.listenTo(actionsModel.selected, 'select', this.updateSelection);
			this.$tabs = this.$('.actions-list');
			this.$delete = new DeleteWidget({
				el: this.$('.model-delete'),
				model: actionsModel.selected
			});
			
			actionsModel.setResource(this.$('#resource-uri').val());
			actionsModel.fetch();
		},
		
		render: function() {
			var html = '';
			
			actionsModel.each(function(model) {
				html += '<li class="action'
				if (model.cid === actionsModel.selected.cid) html += ' selected';
				html += '" data-cid="'+model.cid+'">'+ model.get('id') +'</li>';
			});
			
			html += '<li class="action add-action">+</li>';
			this.$tabs.html(html);
		},
		
		updateSelection: function() {
			this.$tabs
				.children()
				.removeClass('selected')
				.filter('[data-cid="'+ actionsModel.selected.cid +'"]')
				.addClass('selected');
		},
		
		events: {
			'click .action': 'onSelect',
			'click .add-action': 'onAdd'
		},
		
		onSelect: function(evt) {
			var cid = $(evt.target).closest('.action').attr('data-cid');
			actionsModel.select(cid);
		},
		
		onAdd: function() {
			actionsModel.create();
		}
	});
	
	return new ActionsView();
});