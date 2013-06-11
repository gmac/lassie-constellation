define([
	'./base-m'
], function(BaseSceneModelList) {

	var MatrixModelList = BaseSceneModelList.extend({
		api: 'matrix'
	});

	return new MatrixModelList();
});