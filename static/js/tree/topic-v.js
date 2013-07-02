define([
	'jquery',
	'../common/base-edit-v',
	'./topic-m'
], function($, BaseEditView, topicsModel) {
	
	var TopicsView = BaseEditView.extend({
		el: '#topic-manager',
		
		initialize: function() {
			this.model = topicsModel.selected;
			this.listenTo(this.model, 'reset', this.render);
		},
		
		render: function() {
			this.$('.topic-list').html(topicsModel.reduce(function(memo, model) {
				memo += '<li>'+ model.id +'</li>';
				return memo;
			}, ''));
			
			this.populate();
		},
		
		events: function() {
			return {
				'click .add-model': 'onAdd'
			};
		},
		
		onAdd: function() {
			topicsModel.create();
		}
	});
	
	return new TopicsView();
});