define([
	'../common/base-edit-v',
	'./menu-m'
], function(BaseEditView, menusModel) {
	
	return new BaseEditView({
		el: '#menu-manager',
		collection: menusModel,
		model: menusModel.selected
	});
});