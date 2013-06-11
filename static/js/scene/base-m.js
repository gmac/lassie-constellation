define([
    'backbone',
    'jquery'
], function(Backbone, $) {
    
	var SCENE_ID = $('#scene-id').val();
	
	var SceneModelList = Backbone.Collection.extend({
		api: '',
		model: Backbone.Model,

		url: function() {
			return '/api/v1/'+ this.api +'/';
		},
		
		sceneUrl: function() {
			return '/api/v1/scene/'+ SCENE_ID +'/';
		},
		
		getNewSlug: function() {
			if (!this.model) return 'new_object';
			
			var slug = this.api;
			var inc = 0;
			
			this.each(function(model) {
				var modelSlug = model.get('slug');
				if (modelSlug.indexOf(slug) === 0) {
					var modelInc = parseInt(modelSlug.slice(slug.length), 10);
					inc = Math.max(inc, isNaN(modelInc) ? inc : modelInc+1);
				}
			});
			
			return slug + inc;
		},
		
		getNewModel: function() {
			return {
				slug: this.getNewSlug(),
				scene: this.sceneUrl()
			};
		},
		
		create: function() {
			var data = this.getNewModel();
			Backbone.Collection.prototype.create.call(this, data);
			return this.where(data);
		},
		
		sync: function(method, model, options) {
			options.data = options.data || {};
			options.data.scene__id = SCENE_ID;
			options.data.format = 'json';
			Backbone.sync(method, model, options);
		},
		
		parse: function(data) {
			return data.objects;
		},
		
		comparator: function(model) {
			return model.get('slug');
		},
		
		select: function(model) {
			if (model && !(model instanceof Backbone.Model)) {
				model = this.get(model);
			}
			this.trigger('select', model);
		}
	});
	
	SceneModelList.SCENE_ID = SCENE_ID;
	
	return SceneModelList;
});