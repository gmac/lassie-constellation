define([
	'./base-edit-v',
	'../model/grid-m',
	'../grid/grid'
], function(BaseEditView, gridModel, gridController) {
    
	var GridEditView = BaseEditView.extend({
		el: '#grid-edit',
		
		initialize: function() {
			this.setModel(gridModel);
		},
		
		events: {
			'click .cancel': 'onCancel',
			'click .join': 'onJoin',
			'click .split': 'onSplit',
			'click .polygon': 'onPolygon',
			'click .remove': 'onRemove'
		},
		
		onJoin: function() {
			gridController.joinNodes();
		},
		
		onSplit: function() {
			gridController.splitNodes();
		},
		
		onPolygon: function() {
			gridController.makePolygon();
		},
		
		onRemove: function() {
			gridController.deleteGeometry();
		}
	});
	
	return new GridEditView();
});