define([
	'./base-list-v',
	'../model/layer-m'
], function(BaseListView, layersModel) {
    
	var LayersListView = BaseListView.extend({
		el: '#layer-list',
		
		render: function() {
			this.tmpl = this.tmpl || _.template($('#layer-list-item').html());
			
			this.$('.list').html(layersModel.reduce(function(memo, item) {
				return memo + this.tmpl({
					cid: item.cid,
					slug: item.get('slug')
				});
			}, '', this));
		},
		
		onEdit: function(evt) {
			var cid = $(evt.target).closest('.layer').attr('data-cid');
			this.collection.select(cid, true);
		}
	});

	return new LayersListView({
		collection: layersModel,
		model: layersModel.selected
	});
});