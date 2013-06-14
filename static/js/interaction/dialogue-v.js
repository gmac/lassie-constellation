define([
	'backbone',
	'jquery',
	'common/delete-v',
	'./dialogue-m'
], function(Backbone, $, DeleteWidget, dialogueModel) {
	
	var selectedModel = dialogueModel.selected;
	
	var DialogueView = Backbone.View.extend({
		el: '#dialogue-manager',
		
		initialize: function() {
			this.listenTo(dialogueModel, 'add remove reset sync', this.render);
			this.listenTo(selectedModel, 'select', this.render);
			
			this.$delete = new DeleteWidget({
				el: this.$('#dialogue-delete'),
				model: dialogueModel.selected
			});
		},
		
		render: function() {
			if (!selectedModel.model) return;

			this.$('.dialogue-list').html(dialogueModel.reduce(function(memo, model, index) {
				var selected = (model.cid === selectedModel.cid);
				memo += '<li class="action'+ (selected ? ' selected' : '') +'" data-cid="'+model.cid+'">';
				memo += (model.get('puppet') || 'puppet') +': '+ model.get('subtitle') +'</li>';
				return memo;
			}, ''));
		},
		
		events: {
			'click .add-dialogue': 'onAdd',
			'click .dialogue-list li': 'onSelect'
		},
		
		onAdd: function() {
			dialogueModel.create();
		},
		
		onSelect: function(evt) {
			dialogueModel.select($(evt.currentTarget).attr('data-cid'));
		}
	});
	
	return new DialogueView();
});