define([
	'./model/layer-m',
	'./model/grid-m',
	'./model/matrix-m',
	'./toolbar/main',
	'./layer/layer-layout-v',
	'./layer/layer-metrics-v',
	'./grid/grid-layout-v'
], function(layerModel, gridModel, matrixModel) {
	var RESET = layerModel.RESET;
	layerModel.fetch(RESET);
	gridModel.fetch(RESET);
	matrixModel.fetch(RESET);
});