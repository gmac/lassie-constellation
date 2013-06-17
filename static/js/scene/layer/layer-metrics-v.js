define([
	'backbone',
	'jquery',
	'underscore',
	'../model/layer-m'
], function(Backbone, $, _, layerModel) {
	
	var selectedModel = layerModel.selected;
	
	var LayerMetricsView = Backbone.View.extend({
		el: '#layer-metrics',
		
		initialize: function() {
			this.listenTo(selectedModel, 'select', this.render);
			this.listenTo(selectedModel, 'change', this.render);
			this.listenTo(selectedModel, 'edit', this.show);
			this.listenTo(selectedModel, 'cancel', this.hide);
			this.$pos = this.$('.drag');
			this.$size = this.$('.resize');
			this.$map = this.$('.map-pt');
			this.$reg = this.$('.reg-pt');
			this.hide();
		},
		
		show: function() {
			this.$el.show();
		},
		
		hide: function() {
			this.$el.hide();
		},
		
		render: function() {
			this.updatePos();
			this.updateSize();
			this.updateMap();
			this.updateReg();
		},
		
		updatePos: function() {
			this.$pos.css({
				left: selectedModel.get('img_x'),
				top: selectedModel.get('img_y')
			});
		},
		
		updateSize: function() {
			this.$size.css({
				left: selectedModel.get('img_x') + selectedModel.get('img_w'),
				top: selectedModel.get('img_y') + selectedModel.get('img_h')
			});
		},
		
		updateMap: function() {
			this.$map.css({
				left: selectedModel.get('map_x'),
				top: selectedModel.get('map_y')
			});
		},
		
		updateReg: function() {
			this.$reg.css({
				left: selectedModel.get('float_x'),
				top: selectedModel.get('float_y')
			});
		},
		
		events: {
			'mousedown .metric': 'onDragPt'
		},
		
		onDragPt: function(evt) {
			evt.preventDefault();
			var $target = $(evt.target).closest('.metric');
			var offset = $('.viewport').offset();
			var attr = $target.attr('data-attr');
			
			function drag(x, y) {
				x -= (offset.left - 5);
				y -= (offset.top - 5);
				
				$target.css({
					left: x,
					top: y
				});
				
				var data = {};
				if (attr != 'size') {
					data[attr+'_x'] = x;
					data[attr+'_y'] = y;
				} else {
					data['img_w'] = x - selectedModel.get('img_x');
					data['img_h'] = y - selectedModel.get('img_y');
				}
				
				selectedModel.set(data);
			}
			
			function drop() {
				selectedModel.save();
			}
			
			var $win = $(window).on('mousemove.drag', function(evt) {
				drag(evt.pageX, evt.pageY);
			}).on('mouseup.drag', function(evt) {
				$win.off('mousemove.drag mouseup.drag');
				drop();
			});
		}
	});
	
	return new LayerMetricsView();
});