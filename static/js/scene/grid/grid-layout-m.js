/**
* Grid Model.
* Main application model for managing node and polygon data.
*/
define([
	'backbone',
	'underscore',
	'libs/constellation',
	'../model/grid-m'
], function( Backbone, _, Const, gridModel ) {
	
	var updateMethods = [
		'addNode',
		'joinNodes',
		'splitNodes',
		'removeNodes',
		'addPolygon',
		'removePolygons',
		'reset'
	];
	
	var gridViewModel = _.extend(new Const.Grid(), Backbone.Events, {
		
		init: function() {
			var self = this;
			
			// Override all grid mutators with event-firing method wrappers:
			_.each(updateMethods, function(methodName) {
				self[ methodName ] = function() {
					Const.Grid.prototype[ methodName ].apply(self, arguments);
					self.update();
				};
			});
			
			return this;
		},

		// Loads current cache selection into the model:
		load: function() {
			var data = gridModel.selected.get('data') || '';
			this.reset(JSON.parse(data) || {});
		},
		
		// Saves current model data into the cache:
		save: function() {
			gridModel.selected.set('data', this.toJSON());
		},
		
		update: function() {
			this.save();
			this.trigger('change');
		}
	});
	
	return gridViewModel.init();
});