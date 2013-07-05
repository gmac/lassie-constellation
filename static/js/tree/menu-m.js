define([
	'../common/resource-m'
], function(ResourceModel) {
	
	var TreeMenuModel = ResourceModel.extend({
		api: 'treemenu',
		TREE_ID: 0,
		
		getNewModelData: function() {
			return {
				tree: this.formatUri('tree', this.TREE_ID)
			};
		},
		
		getRequestData: function() {
			return {
				tree: this.formatUri('tree', this.TREE_ID),
				format: 'json'
			};
		}
	});
	
	return new TreeMenuModel();
});