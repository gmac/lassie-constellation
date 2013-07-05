define([
	'backbone',
	'underscore',
	'../common/resource-m',
	'./menu-m'
], function(Backbone, _, ResourceModel, menusModel) {
	
	var TopicsModel = ResourceModel.extend({
		api: 'treetopic',
		currentMenu: [],
		TREE_ID: 0,
		
		
		initialize: function() {
			this.listenTo(menusModel.selected, 'select', this.reloadMenu);
			//this.listenTo(this, 'destroy', this.resetOrder);
		},
		
		// Reloads the topics menu state:
		// Menu topics are a subset belonging to the selected menu.
		// Selected topic must be reassessed when toggling menus.
		reloadMenu: function() {
			var menuUri = this.formatUri(menusModel.api, menusModel.selected.get('id'));
			
			// Pick new menu items:
			this.currentMenu = this.where({menu: menuUri});
			
			// Set new selection:
			if (!_.contains(this.currentMenu, this.selected.model)) {
				this.select(this.currentMenu.length ? this.currentMenu[0].id : null);
			}
		},
		
		getNewModelData: function() {
			return {
				index: this.length,
				tree: this.formatUri('tree', this.TREE_ID),
				menu: this.formatUri('treemenu', menusModel.selected.get('id'))
			};
		},
		
		getRequestData: function() {
			return {
				tree: this.formatUri('tree', this.TREE_ID),
				menu: this.formatUri('treemenu', menusModel.selected.get('id')),
				format: 'json'
			};
		}
	});
	
	return new TopicsModel();
});