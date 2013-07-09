define([
	'backbone',
	'underscore',
	'../common/resource-m',
	'../action/action-m'
], function(Backbone, _, ResourceModel, actionsModel) {
	
	var TREE_ID = '';
	var menusModel, topicsModel;
	
	// Tree Menus
	var MenusModel = ResourceModel.extend({
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
				tree: this.formatUri('tree', TREE_ID)
			};
		},
		
		getRequestData: function() {
			return {
				tree: this.formatUri('tree', TREE_ID),
				format: 'json'
			};
		}
	});
	
	// Tree Topics
	var TopicsModel = ResourceModel.extend({
		api: 'treetopic',

		initialize: function() {
			this.listenTo(menusModel.selected, 'select', this.onReset);
			this.listenTo(this.selected, 'select', this.onSelect);
			//this.listenTo(this, 'destroy', this.resetOrder);
		},
		
		getCurrentMenu: function() {
			var menuUri = this.formatUri(menusModel.api, menusModel.selected.get('id'));
			
			// Pick current menu items, sorted by index:
			return this.where({menu: menuUri}).sort(function(a, b) {
				return b.get('index') < a.get('index');
			});
		},
		
		// Reloads the topics menu state:
		// Menu topics are a subset belonging to the selected menu.
		// Selected topic must be reassessed when toggling menus.
		onReset: function() {
			// Select new default item:
			var menu = this.getCurrentMenu();
			this.select(menu.length ? menu[0].id : null);
		},
		
		onSelect: function() {
			var id = this.selected.get('id');
			if (id) {
				actionsModel.load(this.formatUri('treetopic', id));
			} else {
				// disable actions.
			}
		},
		
		getNewModelData: function() {
			return {
				index: this.length,
				tree: this.formatUri('tree', TREE_ID),
				menu: this.formatUri('treemenu', menusModel.selected.get('id'))
			};
		},
		
		getRequestData: function() {
			return {
				tree: this.formatUri('tree', TREE_ID),
				menu: this.formatUri('treemenu', menusModel.selected.get('id')),
				format: 'json'
			};
		}
	});
	
	menusModel = new MenusModel();
	topicsModel = new TopicsModel();
	
	return {
		menus: menusModel,
		topics: topicsModel,
		
		load: function(treeId, menus, topics) {
			TREE_ID = treeId;
			menusModel.reset(menus);
			topicsModel.reset(topics);
		},
		
		expandTopic: function() {
			var topic = topicsModel.selected.model;
			if (!topic) return;
			
			var menu = menusModel.findWhere({topic: topic.get('resource_uri')});
			
			if (menu) {
				menusModel.select(menu.cid);
			} else {
				menu = menusModel.create({topic: topic.get('resource_uri')});
			}
		},
		
		retractMenu: function() {
			var currentMenu = menusModel.selected.model;
			if (!currentMenu) return;
			
			// Find parent topic above current menu:
			var parentTopic = topicsModel.findWhere({resource_uri: currentMenu.get('topic')});
			if (!parentTopic) return;
			
			// Find parent topic's parent menu:
			var parentMenu = menusModel.findWhere({resource_uri: parentTopic.get('menu')});
			if (!parentMenu) return;
			
			// Select parent menu:
			menusModel.select(parentMenu.cid);
		}
	};
});