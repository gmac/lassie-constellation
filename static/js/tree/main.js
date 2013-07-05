define([
	'./menu-m',
	'./topic-m',
	'./menu-v',
	'./topic-v'
], function(menusModel, topicsModel) {
	return {
		load: function(treeId, menus, topics) {
			menusModel.TREE_ID = topicsModel.TREE_ID = treeId;
			
			// Reset topics FIRST so they'll be ready when a topic is selected:
			menusModel.reset(menus);
			topicsModel.reset(topics);
		}
	};
});