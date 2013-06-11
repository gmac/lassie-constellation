define([
    'jquery',
	'./layer-m',
	'./grid-m',
	'./matrix-m'
], function($, layerModel, gridModel, matrixModel) {
	
	function ToolbarViewController() {
		this.listView = $('#toolbar-list');
		this.editView = $('#toolbar-edit').hide();
		layerModel.on('select', this.onSelect, this);
		gridModel.on('select', this.onSelect, this);
		matrixModel.on('select', this.onSelect, this);
	}
	
	ToolbarViewController.prototype = {
		onSelect: function(model) {
			if (model) {
				var api = model.collection.api;
				console.log(api);
				
				this.editView
					.children()
					.hide()
					.filter('[data-api="'+api+'"]')
					.show();
			}
			this.listView.toggle(!model);
			this.editView.toggle(!!model);
		}
	};
	
	return new ToolbarViewController();
});