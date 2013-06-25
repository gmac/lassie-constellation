define([
	'./grid',
	'./grid-layout-m',
	'./grid-layout-v'
], function(gridAPI, gridModel, gridView) {
	gridModel.load();
	return gridAPI;
});