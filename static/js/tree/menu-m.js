define([
	'../common/resource-m'
], function(ResourceModel) {
	
	var TreeMenuModel = ResourceModel.extend({
		api: 'treemenu',
		treeUri: '',
		menuPath: '',
		
		load: function(treeUri, data) {
			this.treeUri = treeUri;
			this.menuPath = '0';
			this.reset(data);
		},
		
		getNewModelData: function() {
			return {
				path: this.menuPath,
				tree: this.treeUri
			};
		},
		
		getRequestData: function() {
			return {
				tree__id: this.MENU_ID,
				format: 'json'
			};
		}
	});
	
	return new TreeMenuModel();
});