define([
	'backbone',
	'jquery',
	'underscore',
	'common/delete-v',
	'common/base-edit-v',
	'./dialogue-m'
], function(Backbone, $, _, DeleteWidget, BaseEditView, dialogueModel) {
	
	var selectedModel = dialogueModel.selected;
	
	var DialogueView = BaseEditView.extend({
		el: '#dialogue-manager',
		
		initialize: function() {
			this.model = dialogueModel.selected;
			this.listenTo(dialogueModel, 'add remove reset', this.render);
			this.listenTo(selectedModel, 'select', this.render);
			this.listenTo(selectedModel, 'change:subtitle', this.renderOptions);
			this.renderVoices();
			
			// Create delete widget:
			this.$delete = new DeleteWidget({
				el: this.$('#dialogue-delete'),
				model: dialogueModel.selected
			});
		},
		
		// Populate voice options selector:
		// should only need to happen once during startup.
		renderVoices: function() {
			this.$('#dialogue-voice').html(dialogueModel.voices.reduce(function(memo, model) {
				return memo += '<option value="'+ model.get('id') +'">'+ model.get('title') +'</option>';
			}, ''));
		},
		
		render: function() {
			this.renderOptions();
			this.populate();
			
			this.$('.dialogue-edit').css({
				opacity: selectedModel.model ? 1 : 0.5,
				pointerEvents: selectedModel.model ? 'auto' : 'none'
			});
		},
		
		renderOptions: function() {
			this.$('.dialogue-list').html(dialogueModel.reduce(function(memo, model, index) {
				var selected = (model.cid === selectedModel.cid);
				memo += '<li class="action'+ (selected ? ' selected' : '') +'" data-cid="'+model.cid+'">';
				memo += (model.get('puppet') || 'puppet') +': '+ (model.get('subtitle') || '') +'</li>';
				return memo;
			}, ''));
		},
		
		events: function() {
			return _.extend({
				'click .add-dialogue': 'onAdd',
				'click .dialogue-list li': 'onSelect'
			}, BaseEditView.prototype.events);
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