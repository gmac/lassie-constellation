define([
	'../common/resource-m'
], function(ResourceModel) {
	
	var TreeMenuModel = ResourceModel.extend({
		api: 'treemenu',
		TREE_ID: 0,
		
		onReset: function() {
			// Get the root menu (no parent topic) as the default.
			var item = this.where({topic: null})[0];
			if (item) this.select(item.id);
			else this.select(0);
		},
		
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