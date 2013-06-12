define([
	'./base-m'
], function(SceneModelList) {

	var MatrixModelList = SceneModelList.extend({
		api: 'matrix'
	});

	return new MatrixModelList();
});