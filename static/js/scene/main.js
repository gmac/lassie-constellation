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
	
	// Configure window resizing:
	var $win = $(window);
	var $scene = $('#scene-edit');
	var resize = function() { $scene.height($win.height()); };
	$win.on('resize', resize);
	resize();
	
	// Load all models:
	var RESET = layerModel.RESET;
	layerModel.fetch(RESET);
	gridModel.fetch(RESET);
	matrixModel.fetch(RESET);
});