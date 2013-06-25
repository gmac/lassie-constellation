define([
	'backbone',
	'../common/resource-m'
], function(Backbone, ResourceModel) {
	
	var TopicsModel = ResourceModel.extend({
		api: 'topic',
		menu: '',
		menus: new Backbone.Collection(),
		
		load: function(treeUri) {
			this.TREE_URI = treeUri;
		},
		
		
		
		getMenuUri: function() {
			return '/api/v1/treemenu/'+ this.MENU_ID +'/';
		},
		
		getNewModelData: function() {
			return {
				index: this.length,
				treemenu: this.getSceneUri()
			};
		},
		
		getRequestData: function() {
			return {
				treemenu__id: this.MENU_ID,
				format: 'json'
			};
		}
	});
	
	return new TopicsModel();
});