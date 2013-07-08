define([
	'../common/base-edit-v',
	'./tree-m'
], function(BaseEditView, treeModel) {
	
	return new BaseEditView({
		el: '#menu-manager',
		collection: treeModel.menus,
		model: treeModel.menus.selected
	});
});