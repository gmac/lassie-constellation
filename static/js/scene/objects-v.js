define([
	'backbone',
    'jquery',
	'underscore',
	'./objects-m'
], function(Backbone, $, _, objectsModel) {
    
	var ObjectsListView = Backbone.View.extend({
		el: '#objects-list',
		
		initialize: function() {
			this.listenTo(objectsModel, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			this.tmpl = this.tmpl || _.template($('#objects-list-item').html());
			
			objectsModel.each(function(item, index) {
				html += this.tmpl({
					cid: item.cid,
					uid: item.get('uid')
				});
			}, this);
			
			this.$('.layers').html(html);
		},
		
		getModelForEl: function(el) {
			var el = $(el).closest('.layer');
			return objectsModel.get(el.attr('data-cid'));
		},
		
		events: {
			'click .add': 'onAdd',
			'click .save': 'onSave',
			'click .remove': 'onRemove',
			'dblclick input': 'onEditId',
			'blur input': 'onCancelId',
			'mousedown .drag': 'onDrag'
		},
		
		onAdd: function() {
			objectsModel.create();
		},
		
		onSave: function() {
			objectsModel.save();
		},
		
		onRemove: function(evt) {
			var model = this.getModelForEl(evt.target);
			model && model.destroy();
		},
		
		onEditId: function(evt) {
			$(evt.target).prop('readonly', false);
		},
		
		onCancelId: function(evt) {
			var input = $(evt.target);
			var model = this.getModelForEl(input);
			model && model.set('uid', input.val());
			input.prop('readonly', true);
		},
		
		onDrag: function(evt) {
			evt.preventDefault();
			var layer = $(evt.target).closest('.layer').addClass('dragging');
			var list = layer.parent();
			var items = list.children();
			var itemH = layer.outerHeight();
			var hilite = layer;
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
				layer.removeClass('dragging');
				
				if (layer.index() != index) {
					if (after) {
						items.eq(index).after(layer);
					} else {
						items.eq(index).before(layer);
					}
				}
				
				items.each(function() {
					var item = $(this);
					objectsModel.get(item.attr('data-cid')).set('index', item.index());
				});
				
				objectsModel.reorder();
			}
			
			$(document)
				.on('mousemove.layer', function(evt) {
					drag(evt.pageY);
				})
				.on('mouseup.layer', function(evt) {
					$(document).off('mousemove.layer mouseup.layer');
					drop();
				});
			
			drag(evt.pageY);
		}
	});

	return new ObjectsListView();
});