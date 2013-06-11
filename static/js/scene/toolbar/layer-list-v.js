define([
	'backbone',
    'jquery',
	'underscore',
	'../model/layer-m'
], function(Backbone, $, _, layersModel) {
    
	var LayersListView = Backbone.View.extend({
		el: '#layer-list',
		
		initialize: function() {
			this.listenTo(layersModel, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			this.tmpl = this.tmpl || _.template($('#layer-list-item').html());
			
			layersModel.each(function(item, index) {
				html += this.tmpl({
					cid: item.cid,
					slug: item.get('slug')
				});
			}, this);
			
			this.$('.list').html(html);
		},
		
		getModelForEl: function(el) {
			var el = $(el).closest('.layer');
			return layersModel.get(el.attr('data-cid'));
		},
		
		events: {
			'click .add': 'onAdd',
			'click .edit': 'onEdit',
			'click .remove': 'onRemove',
			'dblclick input': 'onEditId',
			'blur input': 'onCancelId',
			'mousedown .drag': 'onDrag'
		},
		
		onAdd: function(evt) {
			layersModel.create();
		},
		
		onEdit: function(evt) {
			var model = this.getModelForEl(evt.target);
			layersModel.select(model, true);
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
			model && model.save('slug', input.val(), {patch: true});
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
				
				if (layer.index() == index) return;
				
				if (after) {
					items.eq(index).after(layer);
				} else {
					items.eq(index).before(layer);
				}
				
				list.children().each(function(index) {
					layersModel.get($(this).attr('data-cid')).set('index', index);
				});
				
				layersModel.reorder();
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

	return new LayersListView();
});