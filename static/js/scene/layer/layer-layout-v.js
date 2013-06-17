define([
	'backbone',
	'underscore',
	'../model/layer-m'
], function(Backbone, _, layerModel) {
	
	var LayerView = Backbone.View.extend({
		tagName: 'div',
		className: 'layer',
		
		initialize: function() {
			this.listenTo(this.model, 'change', this.render);
		},
		
		render: function() {
			return this.$el.css({
				left: this.model.get('img_x'),
				top: this.model.get('img_y'),
				width: this.model.get('img_w'),
				height: this.model.get('img_h'),
				opacity: this.model.get('opacity')/100
			});
		}
	});
	
	var LayerLayoutView = Backbone.View.extend({
		el: '#layers-layout',
		views: {},
		
		initialize: function() {
			this.listenTo(layerModel, 'reset', this.render);
			this.listenTo(layerModel, 'add', this.addLayer);
			this.listenTo(layerModel, 'remove', this.removeLayer);
		},
		
		render: function() {
			// remove all existing layers....
			_.each(_.keys(this.views), function(id) {
				this.removeLayer(id);
			}, this);
			
			// Add new layers:
			layerModel.each(function(model) {
				this.addLayer(model);
			}, this);
			
			this.reorder();
		},
		
		// Adds a new layer view to the layout:
		addLayer: function(model) {
			if (!this.views[model.cid]) {
				var layer = new LayerView({
					model: model
				});
				this.views[model.cid] = layer;
				this.$el.append(layer.render());
			}
		},
		
		// Removes a layer view from the layout:
		removeLayer: function(model) {
			if (this.views[model.cid]) {
				this.views[model.cid].remove();
				delete this.views[model.cid];
			}
		},
		
		// Applies z-indexing to the layer order:
		reorder: function() {
			
		}
	});
	
	return new LayerLayoutView();
});