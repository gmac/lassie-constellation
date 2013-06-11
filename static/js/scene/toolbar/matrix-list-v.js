define([
	'./base-list-v',
	'../model/matrix-m'
], function(BaseListView, matrixModel) {
    
	var MatrixListView = BaseListView.extend({
		el: '#matrix-list',
		
		initialize: function() {
			this.setModel(matrixModel);
		}
	});
	
	return new MatrixListView();
});