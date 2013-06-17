define([
	'./base-m'
], function(SceneModelList) {
	
	var MatrixModel = Backbone.Model.extend({
		defaults: {
			notes: '',
			type: 0,
			axis: 0,
			a_x: 0,
			a_y: 0,
			a_value: '',
			b_x: 0,
			b_y: 0,
			b_value: ''
		}
	});
	
	var MatrixModelList = SceneModelList.extend({
		api: 'matrix',
		model: MatrixModel
	});

	return new MatrixModelList();
});