define([
	'backbone',
	'jquery',
	'underscore',
	'common/delete-v',
	'./action-m'
], function(Backbone, $, _, DeleteWidget, actionsModel) {
	
	var selectedModel = actionsModel.selected;
	
	var ActionsView = Backbone.View.extend({
		el: '#actions-manager',
		
		initialize: function() {
			// Pull resource URI from template form:
			var uri = this.$('#resource-uri').val();
			var types = JSON.parse(this.$('#resource-types').val());
			var items = JSON.parse(this.$('#resource-items').val());
			
			if (!uri) {
				this.$el.hide();
				return;
			}
			
			_.each(types, function(model) {
				model.id = '/api/v1/action_type/'+model.id+'/';
			});
			
			_.each(items, function(model) {
				model.id = '/api/v1/item/'+model.id+'/';
			});
			
			this.setup();
			actionsModel.types.reset(types);
			actionsModel.items.reset(items);
			actionsModel.setResource(uri);
			actionsModel.fetch();
		},
		
		setup: function() {
			this.listenTo(selectedModel, 'select', this.render);
			this.listenTo(selectedModel, 'change:action_type', this.render);
			
			this.$tabs = this.$('.actions-list');
			this.$types = this.$('#action-type');
			
			this.$delete = new DeleteWidget({
				el: this.$('.model-delete'),
				model: selectedModel
			});
		},
		
		render: function() {
			// Abort if there's no selected model (something went wrong)...
			if (!selectedModel.model) return;
			
			var html = '';
			var selectedType = actionsModel.types.get(selectedModel.get('action_type'));
			var selectedItem = actionsModel.items.get(selectedModel.get('related_item') || '');
			
			// Render action tab options:
			actionsModel.sort();
			actionsModel.each(function(model) {
				// Get type and related item models:
				var type = actionsModel.types.get(model.get('action_type') || '');
				var item = actionsModel.items.get(model.get('related_item') || '');
				var label = type.get('is_generic') ? model.get('slug') : type.get('title');
				if (item && type.get('is_item')) {
					item = item.get('slug');
				}

				html += '<li class="action';
				if (model.cid === selectedModel.cid) html += ' selected';
				html += '" data-cid="'+model.cid+'">'+ (label || 'Untitled') +'</li>';
			});
			
			html += '<li class="action add-action">+</li>';
			this.$tabs.html(html);
			
			// Render action type options:
			html = '';
			var selected = actionsModel.pluck('action_type');
			actionsModel.types.each(function(type) {
				var current = (type.id === selectedType.id);
				if (current || type.get('is_generic') || type.get('is_item')  || !_.contains(selected, type.id)) {
					html += '<option value="'+ type.id +'" data-cid="'+ type.cid +'"';
					if (current) html += ' selected="selected"';
					html += '>'+ type.get('title') +'</option>';
				}
			});
			
			this.$types.html(html);
			
			// Toggle dependent field visibility:
			this.$('.action-item').toggle(!!selectedItem);
			this.$('.action-slug').toggle(selectedType.get('is_generic'));
		},
		
		events: {
			'click .action': 'onSelect',
			'click .add-action': 'onAdd',
			'change #action-type': 'onSetType'
		},
		
		onSelect: function(evt) {
			var cid = $(evt.target).closest('.action').attr('data-cid');
			actionsModel.select(cid);
		},
		
		onAdd: function() {
			actionsModel.create();
		},
		
		onSetType: function() {
			selectedModel.set('action_type', this.$types.val());
		}
	});
	
	return new ActionsView();
});