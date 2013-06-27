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
			this.listenTo(dialogueModel, 'add remove reset sort', this.render);
			this.listenTo(selectedModel, 'change:title change:voice change:slug', this.renderOptions);
			this.listenTo(selectedModel, 'select', this.render);
			this.makeDragable('.dialogue-list', '.dragable');
			this.$list = this.$('.dialogue-list');
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
			this.$list.html(dialogueModel.reduce(function(memo, model, index) {
				var selected = (model.cid === selectedModel.cid);
				var voice = dialogueModel.voices.get(model.get('voice'));
				var slug = model.get('slug');
				memo += '<li class="action'+ (selected ? ' selected' : '') +'" data-cid="'+model.cid+'">';
				memo += '<span class="dragable">['+ index + (slug ? ':'+slug : '') +']</span> ';
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
	
	return new DialogueView({
		collection: dialogueModel,
		model: dialogueModel.selected
	});
});