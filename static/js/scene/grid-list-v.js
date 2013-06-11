define([
	'backbone',
    'jquery',
	'underscore',
	'./grid-m',
	'./matrix-m'
], function(Backbone, $, _, gridsModel, matricesModel) {
    
	var GridListView = Backbone.View.extend({
		el: '#grid-list',
		
		initialize: function() {
			this.listenTo(gridsModel, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			gridsModel.each(function(model) {
				html += '<option value="'+ model.get('slug') +'">'+ model.get('slug') +'</option>';
			});
			this.$('.list').html(html);
		},
		
		events: {
			'click .add': 'onAdd'
		},
		
		onAdd: function() {
			var model = gridsModel.create();
			this.$('.list').val( model.get('slug') );
		}
	});
	

	var MatrixListView = Backbone.View.extend({
		el: '#matrix-list',
		
		initialize: function() {
			this.listenTo(matricesModel, 'add remove reset sync', this.render);
		},
		
		render: function() {
			var html = '';
			matricesModel.each(function(model) {
				html += '<option value="'+ model.get('slug') +'">'+ model.get('slug') +'</option>';
			});
			this.$('.list').html(html);
		},
		
		events: {
			'click .add': 'onAdd'
		},
		
		onAdd: function() {
			var model = matricesModel.create();
			this.$('.list').val( model.get('slug') );
		}
	});
	
	new MatrixListView();
	
	return new GridListView();
});