define([
	'backbone',
	'jquery'
], function(Backbone, $) {
	
	var PATCH = {patch:true};
	
	var BaseEditView = Backbone.View.extend({
		initialize: function() {
			this.listenTo(this.model, 'select', this.populate);
		},
		
		populate: function() {
			var model = this.model;
			if (!model) return;
			
			this.$('[name]').each(function() {
				this.value = model.get(this.name) || '';
			});
		},
		
		// Makes list items draggable:
		// requires a collection resource of models with an "index" property.
		makeDragable: function(ulSelector, gripSelector, equalRowHeights) {
			if (!this.collection) return;
			
			var self = this;
			var $list = this.$(ulSelector).on('mousedown', gripSelector, function(evt) {
				self.fDragItem(evt, self.collection, equalRowHeights);
			});
		},
		
		confirmDelete: function(confirm) {
			this.$('> .delete-cancel').toggle(!confirm);
			//this.$('> .delete-confirm').toggle(confirm);
		},
		
		events: {
			'change .slug-field': 'fSlug',
			'change .text-field': 'fValue',
			'change .select-field': 'fValue',
			'change .integer-field': 'fInteger',
			'change .percent-field': 'fPercent',
			'click .delete': 'fDelete',
			'click .cancel-edit': 'fCancel'
		},
		
		// Delete button field:
		fDelete: function(evt) {
			switch ($(evt.currentTarget).attr('data-op')) {
				case 'intent': this.confirmDelete(true); return;
				case 'cancel': this.confirmDelete(false); return;
			}
			this.confirmDelete(false);
			this.model.cancel();
			this.model.destroy();
		},
		
		fCancel: function() {
			this.model.cancel();
		},
		
		// Unvalidated value (free text, select):
		fValue: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = field.val();
			this.model.save(name, value, PATCH);
		},
		
		// Slug value (no spaces, all lowercase):
		fSlug: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = field.val();
			var valid = value.replace(/[\W\s]/g, '_').toLowerCase();
			if (valid !== value) field.val(valid);
			this.model.save(name, valid, PATCH);
		},
		
		fInteger: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = parseInt(field.val(), 10);
			if (isNaN(value)) field.val(this.model.get('name'));
			else this.model.save(name, value, PATCH);
		},
		
		fPercent: function(evt) {
			var field = $(evt.currentTarget);
			var name = field.attr('name');
			var value = parseInt(field.val(), 10);
			var valid = Math.max(0, Math.min(value, 100));
			if (isNaN(value)) {
				field.val(this.model.get('name'));
				return;
			}
			
			if (value !== valid) field.val(valid);
			this.model.save(name, valid, PATCH);
		},
		
		fDragItem: function(evt, indexedModel, equalRowHeights) {
			evt.preventDefault();
			var target = $(evt.target).closest('li').addClass('dragging');
			var list = target.parent();
			var items = list.children();
			var itemH = target.outerHeight();
			var hilite = target;
			var index = -1;
			var after = false;
			
			// Drags an item within the stacking order:
			function drag(pageY) {
				var offset = list.offset();
				var y = pageY - offset.top;
				var i = Math.max(0, Math.min(Math.floor(y/itemH), items.length-1));
				var a = (y > itemH * items.length - itemH / 2);
				
				if (index != i || after != a) {
					index = i;
					after = a;
					hilite.removeClass('hilite');
					hilite = after ? list : items.eq(index);
					hilite.addClass('hilite');
				}
			}
			
			// Drops an item within the stacking order:
			function drop() {
				hilite.removeClass('hilite');
				target.removeClass('dragging');
				
				if (target.index() == index) return;
				
				if (after) {
					items.eq(index).after(target);
				} else {
					items.eq(index).before(target);
				}
				
				list.children().each(function(index) {
					indexedModel.get($(this).attr('data-cid')).set('index', index);
				});
				
				indexedModel.reorder();
			}
			
			$(document)
				.on('mousemove.drag', function(evt) {
					drag(evt.pageY);
				})
				.on('mouseup.drag', function(evt) {
					$(document).off('mousemove.drag mouseup.drag');
					drop();
				});
			
			drag(evt.pageY);
		}
	});
	
	return BaseEditView;
});