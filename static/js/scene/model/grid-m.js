define([
	'./base-m'
], function(SceneModelList) {

	var GridModelList = SceneModelList.extend({
		api: 'grid'
	});

	return new GridModelList();
});