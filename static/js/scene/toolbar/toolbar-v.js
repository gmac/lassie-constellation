define([
	'backbone',    
	'jquery',
	'../model/layer-m',
	'../model/grid-m',
	'../model/matrix-m'
], function(Backbone, $, layerModel, gridModel, matrixModel) {
	
	var ToolbarPanelView = Backbone.View.extend({
		el: '#toolbar',
		
		models: [
			layerModel,
			gridModel,
			matrixModel
		],
		
		initialize: function() {
			var self = this;
			this.$list = this.$('#toolbar-list');
			this.$edit = this.$('#toolbar-edit').hide();
			
			_.each(this.models, function(model) {
				this.listenTo(model.selected, 'edit', this.onEdit);
				this.listenTo(model.selected, 'cancel', this.onCancel);
				model.fetch(model.RESET);
			}, this);
			
			function setHeight() {
				//self.$el.height($win.height());
			}
			
			//var $win = $(window).on('resize', setHeight);
			//setHeight();
		},
		
		onEdit: function(api) {
			if (api) {
				this.$edit
					.children()
					.hide()
					.filter('[data-api="'+api+'"]')
					.show();
			}
			
			this.$list.toggle(!api);
			this.$edit.toggle(!!api);
		},
		
		onCancel: function() {
			this.$list.toggle(true);
			this.$edit.toggle(false);
		}
	});
	
	return new ToolbarPanelView();
});