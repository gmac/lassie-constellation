define([
	'./base-m'
], function(BaseSceneModelList) {

	var GridModelList = BaseSceneModelList.extend({
		api: 'grid'
	});

	return new GridModelList();
});