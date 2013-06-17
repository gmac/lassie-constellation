define([
	'./base-list-v',
	'../model/matrix-m'
], function(ListView, matrixResource) {
    
	return new ListView({
		el: '#matrix-list',
		collection: matrixResource,
		model: matrixResource.selected
	});
});