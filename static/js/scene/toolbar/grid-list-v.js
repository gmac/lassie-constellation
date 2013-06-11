define([
	'./base-list-v',
	'../model/grid-m'
], function(BaseListView, gridsModel) {
    
	var GridListView = BaseListView.extend({
		el: '#grid-list',
		
		initialize: function() {
			this.setModel(gridsModel);
		}
	});
	
	return new GridListView();
});