define([
	'./layer-m',
	'./grid-m',
	'./matrix-m',
    './layer-list-v',
	'./layer-edit-v',
	'./grid-list-v',
	'./toolbar-c'
], function(layersModel, gridsModel, matricesModel) {
    
	layersModel.fetch();
	gridsModel.fetch();
	matricesModel.fetch();
	
});