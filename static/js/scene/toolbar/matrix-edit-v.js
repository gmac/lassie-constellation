define([
	'./base-edit-v',
	'../model/matrix-m'
], function(BaseEditView, matrixModel) {
    
	var MatrixEditView = BaseEditView.extend({
		el: '#matrix-edit',
		
		initialize: function() {
			this.setModel(matrixModel);
		}
	});
	
	return new MatrixEditView();
});