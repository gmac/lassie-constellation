define([
	'backbone'
], function(Backbone) {
	
	var ActionModelList = Backbone.Collection.extend({
		url: '/api/v1/action/',
		contentObject: '/api/v1/xxx/x/',
		
		create: function() {
			Backbone.Collection.prototype.create(this, {
				content_object: this.contentObject,
				index: this.length
			});
		}
	});
	
	return new ActionModelList();
});