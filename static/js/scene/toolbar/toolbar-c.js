define([
    'jquery',
	'../model/layer-m',
	'../model/grid-m',
	'../model/matrix-m',
	'./layer-list-v',
	'./layer-edit-v',
	'./grid-list-v',
	'./grid-edit-v',
	'./matrix-list-v',
	'./matrix-edit-v'
], function($, layerModel, gridModel, matrixModel) {
	
	function ToolbarViewController() {
		this.listView = $('#toolbar-list');
		this.editView = $('#toolbar-edit').hide();
		
		// Capture edit events:
		layerModel.selected.on('edit', this.onEdit, this);
		gridModel.selected.on('edit', this.onEdit, this);
		matrixModel.selected.on('edit', this.onEdit, this);
		
		// Capture cancel events:
		layerModel.selected.on('cancel', this.onCancel, this);
		gridModel.selected.on('cancel', this.onCancel, this);
		matrixModel.selected.on('cancel', this.onCancel, this);
	}
	
	ToolbarViewController.prototype = {
		onEdit: function(api) {
			if (api) {
				this.editView
					.children()
					.hide()
					.filter('[data-api="'+api+'"]')
					.show();
			}
			
			this.listView.toggle(!api);
			this.editView.toggle(!!api);
		},
		
		onCancel: function() {
			this.listView.toggle(true);
			this.editView.toggle(false);
		}
	};
	
	layerModel.fetch();
	gridModel.fetch();
	matrixModel.fetch();
	
	return new ToolbarViewController();
});