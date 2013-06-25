define([
	'backbone',
	'jquery',
	'underscore',
	'common/base-edit-v',
	'./dialogue-m'
], function(Backbone, $, _, BaseEditView, dialogueModel) {
	
	var selectedModel = dialogueModel.selected;
	
	var DialogueView = BaseEditView.extend({
		el: '#dialogue-manager',
		
		initialize: function() {
			this.model = dialogueModel.selected;
			this.listenTo(dialogueModel, 'add remove reset', this.render);
			this.listenTo(selectedModel, 'select', this.render);
			this.listenTo(selectedModel, 'change:title change:voice', this.renderOptions);
		},
		
		// Populate voice options selector:
		// should only need to happen once during startup.
		renderVoices: function() {
			if (this.$voices) return;
			this.$voices = this.$('#dialogue-voice').html(dialogueModel.voices.reduce(function(memo, model) {
				return memo += '<option value="'+ model.get('id') +'">'+ model.get('label') +'</option>';
			}, ''));
		},
		
		render: function() {
			this.renderVoices();
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
				var voice = dialogueModel.voices.get(model.get('voice'));
				memo += '<li class="action'+ (selected ? ' selected' : '') +'" data-cid="'+model.cid+'">';
				if (model.get('slug')) memo += '['+ model.get('slug') +'] ';
				memo += (voice && voice.get('label') || '') +': '+ (model.get('title') || '') +'</li>';
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