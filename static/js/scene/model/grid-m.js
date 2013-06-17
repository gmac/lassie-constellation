define([
	'./base-m'
], function(SceneModelList) {
	
	var GridModel = Backbone.Model.extend({
		defaults: {
			notes: '',
			data: '{}'
		}
	});
	
	var GridModelList = SceneModelList.extend({
		api: 'grid',
		model: GridModel
	});

	return new GridModelList();
});