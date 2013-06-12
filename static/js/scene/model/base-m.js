define([
    'jquery',
	'common/resource-m'
], function($, ResourceModelList) {
    
	var SCENE_ID = $('#scene-id').val();
	
	var SceneModelList = ResourceModelList.extend({
		
		comparator: function(model) {
			return model.get('slug');
		},
		
		getSceneUri: function() {
			return '/api/v1/scene/'+ SCENE_ID +'/';
		},
		
		getNewModelData: function() {
			return {
				slug: this.getNewSlug(),
				scene: this.getSceneUri()
			};
		},
		
		getRequestData: function() {
			return {
				scene__id: SCENE_ID,
				format: 'json'
			};
		}
	});
	
	return SceneModelList;
});