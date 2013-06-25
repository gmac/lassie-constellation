define([
	'backbone',
	'jquery',
	'underscore',
	'common/base-edit-v',
	'./action-m'
], function(Backbone, $, _, BaseEditView, actionsModel) {
	
	var selectedModel = actionsModel.selected;
	
	var ActionsView = BaseEditView.extend({
		el: '#actions-manager',
		
		initialize: function() {
			this.model = selectedModel;
			this.listenTo(selectedModel, 'select change', this.render);
			
			this.$list = this.$('.actions-list');
			this.$types = this.$('#action-type');
			this.$items = this.$('#action-item');
			this.isMultiAction = !!this.$list.length;
			
			if (!actionsModel.types.length || !actionsModel.voices.length) {
				$('#dialogue-manager').hide();
				this.$el.hide();
			} else if (!this.isMultiAction) {
				actionsModel.enableAutoCreate();
			}
		},
		
		render: function() {
			// Set up UI rendering:
			if (this.isMultiAction) {
				// Render multi-action:
				this.renderMultiAction();
			}
			
			this.populate();
		},
		
		// Renders multi-select options:
		// includes multiple actions, action types, and related items.
		renderMultiAction: function() {
			// Render action tab options:
			actionsModel.sort();
			
			var html = '<li class="action add-action">+</li>';
			var hasModel = !!selectedModel.model;
			var selectedType = actionsModel.types.get(selectedModel.get('action_type'));
			
			// Set dependent fields visibility & values:
			// (specifically cast '.length' as boolean for jQuery toggle implementation quirks...)
			this.$('.action-item').toggle(hasModel && selectedType.get('is_item') && Boolean(actionsModel.items.length));
			this.$('.action-slug').toggle(hasModel && selectedType.get('is_custom'));
			this.$('.model-delete').toggle(hasModel);
			this.$('#action-script').prop('disabled', !hasModel);
			this.$('#action-grammar').prop('disabled', !hasModel);
			
			// Empty/disable lists when no type option is available:
			if (!selectedType) {
				this.$list.html(html);
				this.$types.html('').prop('disabled', true);
				this.$items.html('').prop('disabled', true);
				return;
			}
			
			// Render actions list:
			html += actionsModel.reduce(function(memo, model) {
				// Get type and related item models:
				var type = actionsModel.types.get(model.get('action_type') || '');
				var item = actionsModel.items.get(model.get('related_item') || '');
				var label = type.get('label');
				var slug = model.get('slug');

				if (type.get('is_custom') && slug) {
					label += ': '+ slug;
				} else if (type.get('is_item') && item) {
					label += ': '+ item.get('slug');
				}

				memo += '<li class="action';
				if (model.cid === selectedModel.cid) memo += ' selected';
				memo += '" data-cid="'+model.cid+'">'+ (label || 'Untitled') +'</li>';
				return memo;
			}, '');
				
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
				if (current || model.get('is_custom') || model.get('is_item')  || !_.contains(usedTypes, model.id)) {
					memo += '<option value="'+ model.id +'" data-cid="'+ model.cid +'"';
					if (current) memo += ' selected="selected"';
					memo += '>'+ model.get('label') +'</option>';
				}
				return memo;
			}, '')).prop('disabled', false);
			
			
			// Render item options:
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
			}, '')).prop('disabled', false);
		},
		
		events: function() {
			return _.extend({
				'click .action': 'onSelect',
				'click .add-action': 'onAdd',
				'change #action-type': 'onSetType'
			}, BaseEditView.prototype.events);
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
		}
	});
	
	return new ActionsView();
});