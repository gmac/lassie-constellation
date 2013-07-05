define([
	'./menu-m',
	'./topic-m',
	'./menu-v',
	'./topic-v'
], function(menusModel, topicsModel) {
	return {
		setTree: function(id) {
			menusModel.TREE_ID = id;
			topicsModel.TREE_ID = id;
			return this;
		},
		setMenus: function(data) {
			menusModel.reset(data);
			return this;
		},
		setTopics: function(data) {
			topicsModel.reset(data);
			return this;
		}
	};
});