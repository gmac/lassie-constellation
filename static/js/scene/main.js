define([
	'jquery',
	'./model/layer-m',
	'./model/grid-m',
	'./model/matrix-m',
	'./toolbar/main',
	'./layer/layer-layout-v',
	'./layer/layer-metrics-v',
	'./grid/grid-layout-v'
], function($, layerModel, gridModel, matrixModel) {
	
	var scene = $('#scene-editor');
	var win = $(window);
	var resize = function() { scene.height(win.height()); };
	win.on('resize', resize);
	resize();
	
	layerModel.fetch(layerModel.RESET);
	gridModel.fetch(gridModel.RESET);
	matrixModel.fetch(matrixModel.RESET);
});