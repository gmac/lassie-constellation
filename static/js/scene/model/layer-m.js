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
			
			var order = this.map(function(model) {
				return {
					index: model.get('index'),
					resource_uri: model.get('resource_uri')
				};
			});
			
			this.sync('patch', this, {
				data: JSON.stringify({objects: order, format: 'json'}),
				contentType: 'application/json'
			});
		}
	});
	
	return new LayerModelList();
});