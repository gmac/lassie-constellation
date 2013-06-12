define([
	'./base-list-v',
	'../model/grid-m'
], function(ListView, gridsResource) {
    
	return new ListView({
		el: '#grid-list',
		collection: gridsResource
	});
});