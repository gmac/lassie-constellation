define([
	'jquery',
	'underscore',
	'../common/base-edit-v',
	'./menu-m',
	'./topic-m'
], function($, _, BaseEditView, menusModel, topicsModel) {
	
	var TopicsView = BaseEditView.extend({
		el: '#topic-manager',
		
		initialize: function() {
			this.listenTo(topicsModel.selected, 'select', this.render);
		},
		
		render: function() {
			var topics = topicsModel.currentMenu.sort(function(a, b) {
				return b.get('index') < a.get('index');
			});
			
			var selected = topicsModel.selected.cid;
			
			this.$('.topic-list').html(_.reduce(topics, function(memo, model) {
				memo += '<li data-cid="'+ model.cid +'"';
				if (selected === model.cid) memo += ' class="selected"'
				return memo += '>'+ model.get('id') +'</li>';
			}, ''));
		},
		
		events: function() {
			return {
				'click .add-model': 'onAdd',
				'click .topic-list li': 'onSelect'
			};
		},
		
		onAdd: function() {
			topicsModel.create();
		},
		
		onSelect: function(evt) {
			topicsModel.select($(evt.currentTarget).attr('data-cid'));
		}
	});
	
	return new TopicsView({
		collection: topicsModel,
		model: topicsModel.selected
	});
});