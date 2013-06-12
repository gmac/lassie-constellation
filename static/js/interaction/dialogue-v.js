define([
	'backbone',
	'./dialogue-m'
], function(Backbone, dialogueModel) {
	
	var DialogueView = Backbone.View.extend({
		el: '#dialogue-manager',
		
		initialize: function() {
			this.listenTo(dialogueModel, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			dialogueModel.each(function(model) {
				html += '<li class="action" data-cid="'+model.cid+'">'+ model.get('id') +'</li>';
			});
			
			this.$('.dialogue-list').html(html);
		},
		
		events: {
			'click .add-dialogue': 'onAdd'
		},
		
		onAdd: function() {
			dialogueModel.create();
		}
	});
	
	return new DialogueView();
});