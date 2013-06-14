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
			
			if (!uri || !types.length) {
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
			this.listenTo(selectedModel, 'change', this.render);
			
			this.$list = this.$('.actions-list');
			this.$types = this.$('#action-type');
			this.$items = this.$('#action-item');
			this.isMultiAction = !!this.$list.length;
			
			this.$delete = new DeleteWidget({
				el: this.$('#action-delete'),
				model: selectedModel
			});
		},
		
		render: function() {
			// Abort if there's no selected model (something went wrong)...
			if (!selectedModel.model) return;
			if (this.isMultiAction) this.renderMultiAction();
		},
		
		// Renders multi-select options:
		// includes multiple actions, action types, and related items.
		renderMultiAction: function() {
			var selectedType = actionsModel.types.get(selectedModel.get('action_type'));
			
			// Render action tab options:
			actionsModel.sort();
			var html = actionsModel.reduce(function(memo, model) {
				// Get type and related item models:
				var type = actionsModel.types.get(model.get('action_type') || '');
				var item = actionsModel.items.get(model.get('related_item') || '');
				var label = type.get('title');
				var slug = model.get('slug');
				
				if (type.get('is_generic') && slug) {
					label += ': '+ slug;
				} else if (type.get('is_item') && item) {
					label += ': '+ item.get('slug');
				}

				memo += '<li class="action';
				if (model.cid === selectedModel.cid) memo += ' selected';
				memo += '" data-cid="'+model.cid+'">'+ (label || 'Untitled') +'</li>';
				return memo;
			}, '');
			
			html += '<li class="action add-action">+</li>';
			this.$list.html(html);
			
			
			// Render action type options:
			var usedTypes = actionsModel.pluck('action_type');
			this.$types.html(actionsModel.types.reduce(function(memo, model) {
				var current = (model.id === selectedType.id);
				
				// Add option if:
				// - type is selected.
				// - type is generic (allow unlimited).
				// - type is an item (allow unlimited).
				// - type is unused.
				if (current || model.get('is_generic') || model.get('is_item')  || !_.contains(usedTypes, model.id)) {
					memo += '<option value="'+ model.id +'" data-cid="'+ model.cid +'"';
					if (current) memo += ' selected="selected"';
					memo += '>'+ model.get('title') +'</option>';
				}
				return memo;
			}, ''));
			
			
			// Render item options:
			if (selectedType.get('is_item')) {
				var usedItems = actionsModel.pluck('related_item');
				this.$items.html(actionsModel.items.reduce(function(memo, model) {
					var current = (model.id === selectedModel.get('related_item'));
					
					// Add option if:
					// - item is selected (current).
					// - item is unused.
					if (current || !_.contains(usedItems, model.id)) {
						memo += '<option value="'+ model.id +'" data-cid="'+ model.cid +'"';
						if (current) memo += ' selected="selected"';
						memo += '>'+ model.get('slug') +'</option>';
					}
					return memo;
				}, ''));
			}
			
			// Set dependent fields visibility & values:
			this.$('.action-item').toggle(selectedType.get('is_item'));
			this.$('.action-slug').toggle(selectedType.get('is_generic'));
			this.$('#action-slug').val(selectedModel.get('slug') || '');
		},
		
		events: {
			'click .action': 'onSelect',
			'click .add-action': 'onAdd',
			'change #action-type': 'onSetType',
			'change #action-slug': 'onSetSlug',
			'change #action-item': 'onSetItem'
		},
		
		onSelect: function(evt) {
			var cid = $(evt.target).closest('.action').attr('data-cid');
			actionsModel.select(cid);
		},
		
		onAdd: function() {
			actionsModel.create();
		},
		
		onSetType: function() {
			var type = actionsModel.types.get(this.$types.val());
			if (type) {
				// Reset related fields when switching types:
				var defaultItem = actionsModel.getDefaultItem();
				var data = {
					action_type: type.id,
					related_item: type.get('is_item') && defaultItem ? defaultItem.id : null
				};
				if (!type.get('is_generic')) data.slug = '';
				selectedModel.save(data, actionsModel.PATCH);
			}
		},
		
		onSetSlug: function() {
			selectedModel.set('slug', this.$('#action-slug').val() || '');
		},
		
		onSetItem: function() {
			selectedModel.set('related_item', this.$('#action-item').val() || null);
		}
	});
	
	return new ActionsView();
});