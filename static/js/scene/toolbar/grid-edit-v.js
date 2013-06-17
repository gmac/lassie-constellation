define([
	'jquery',
	'common/base-edit-v',
	'../model/grid-m',
	'../grid/grid'
], function($, BaseEditView, gridResource, gridController) {
    
	var GridEditView = BaseEditView.extend({
		el: '#grid-edit',
		
		events: function() {
			return _.extend({
				'click .grid-op': 'onGridOp'
			}, BaseEditView.prototype.events);
		},
		
		onGridOp: function(evt) {
			switch ($(evt.currentTarget).attr('data-op')) {
				case 'join': gridController.joinNodes(); return;
				case 'split': gridController.splitNodes(); return;
				case 'polygon': gridController.makePolygon(); return;
				case 'remove': gridController.deleteGeometry(); return;
			}
		}
	});
	
	return new GridEditView({
		collection: gridResource,
		model: gridResource.selected
	});
});