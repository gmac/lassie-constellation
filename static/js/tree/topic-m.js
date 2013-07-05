define([
	'backbone',
	'underscore',
	'../common/resource-m',
	'../action/action-m',
	'./menu-m'
], function(Backbone, _, ResourceModel, actionsModel, menusModel) {
	
	var TopicsModel = ResourceModel.extend({
		api: 'treetopic',
		currentMenu: [],
		TREE_ID: 0,
		
		
		initialize: function() {
			this.listenTo(menusModel.selected, 'select', this.onReset);
			this.listenTo(this.selected, 'select', this.onSelect);
			//this.listenTo(this, 'destroy', this.resetOrder);
		},
		
		// Reloads the topics menu state:
		// Menu topics are a subset belonging to the selected menu.
		// Selected topic must be reassessed when toggling menus.
		onReset: function() {
			var menuUri = this.formatUri(menusModel.api, menusModel.selected.get('id'));
			
			// Pick new menu items, sorted by index:
			this.currentMenu = this.where({menu: menuUri}).sort(function(a, b) {
				return b.get('index') < a.get('index');
			});
			
			// Select new default item:
			this.select(this.currentMenu.length ? this.currentMenu[0].id : null);
		},
		
		onSelect: function() {
			var id = this.selected.get('id');
			if (id) {
				actionsModel.load(this.formatUri('treetopic', id));
			} else {
				// disable.
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