define([
	'backbone',
	'./base-m'
], function(Backbone, SceneModelList) {
	
	var LayerModel = Backbone.Model.extend({
		defaults: {
			img_x: 0,
			img_y: 0,
			img_w: 100,
			img_h: 100,
			opacity: 50
		}
	});
	
	var LayerModelList = SceneModelList.extend({
		api: 'layer',
		model: LayerModel,
		
		comparator: function(model) {
			return model.get('index');
		},
		
		getNewModelData: function() {
			var data = SceneModelList.prototype.getNewModelData.call(this);
			data.index = this.length;
			return data;
		},
		
		reorder: function() {
			this.sort();
			this.patch(this.map(function(model) {
				return model.pick('resource_uri', 'index');
			}));
		}
	});
	
	return new LayerModelList();
});