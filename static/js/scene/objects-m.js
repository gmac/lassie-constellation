define([
    'backbone',
	'jquery'
], function(Backbone, $) {
	
	var SCENE_ID = $('#scene-id').val();
	
    var SceneObjectModel = Backbone.Model.extend({
		defaults: {
			uid: 'new_object',
			scene: '/scene/api/v1/scene/'+SCENE_ID+'/'
		}
	});

	var SceneObjectList = Backbone.Collection.extend({
		url: '/scene/api/v1/object/',
		model: SceneObjectModel,
		
		sync: function(method, model, options) {
			options.data = options.data || {};
			options.data.scene__id = SCENE_ID;
			options.data.format = 'json';
			Backbone.sync(method, model, options);
		},
		
		parse: function(data) {
			return data.objects;
		},
		
		save: function() {
			$.ajax({
				url: this.url,
				method: 'PUT',
				data: JSON.stringify({objects: this.toJSON()}),
				contentType: 'application/json'
			});
		},
		
		reorder: function() {
			this.models.sort(function(a, b) {
				return a.get('index') - b.get('index');
			});
		}
	});
	
	return new SceneObjectList();
});