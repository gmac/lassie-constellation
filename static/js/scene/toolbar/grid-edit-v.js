define([
	'./base-edit-v',
	'../model/grid-m'
], function(BaseEditView, gridModel) {
    
	var GridEditView = BaseEditView.extend({
		el: '#grid-edit',
		
		initialize: function() {
			this.setModel(gridModel);
		}
	});
	
	return new GridEditView();
});