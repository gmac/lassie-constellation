define([
	'common/base-edit-v',
	'../model/matrix-m'
], function(BaseEditView, matrixResource) {
    
	var MatrixEditView = BaseEditView.extend({
		el: '#matrix-edit'
	});
	
	return new MatrixEditView({
		collection: matrixResource,
		model: matrixResource.selected
	});
});