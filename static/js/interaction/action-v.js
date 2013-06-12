define([
	'backbone',
	'jquery',
	'./action-m'
], function(Backbone, $, actionsModel) {
	
	var ActionsView = Backbone.View.extend({
		el: '#actions-manager',
		
		initialize: function() {
			this.listenTo(actionsModel, 'add remove reset sync', this.render);
			actionsModel.setResource(this.$('#resource-uri').val());
			actionsModel.fetch();
		},
		
		render: function() {
			var actions = '';
			actionsModel.each(function(model) {
				actions += '<li class="action" data-cid="'+model.cid+'">'+ model.get('id') +'</li>';
			});
			
			actions += '<li class="add-action">+</li>';
			this.$('.actions-list').html(actions);
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