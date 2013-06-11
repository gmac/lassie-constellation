define([
	'./layer-m',
	'./grid-m',
	'./matrix-m',
    './layer-list-v',
	'./layer-edit-v',
	'./grid-list-v'
], function(layersModel, gridsModel, matricesModel) {
    
	layersModel.fetch();
	gridsModel.fetch();
	matricesModel.fetch();
	
});