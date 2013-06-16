define([
	'./base-m'
], function(SceneModelList) {

	var LayerModelList = SceneModelList.extend({
		api: 'layer',
		
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