define([
	'backbone',
	'underscore',
	'common/resource-m'
], function(Backbone, _, ResourceModelList) {
	
	var ActionModelList = ResourceModelList.extend({
		api: 'action',
		allowEmpty: false,
		
		// Fill these in using .setResource();
		resourceId: 0,
		resourceURI: '/api/v1/xxx/x/',
		
		// Related Model collections:
		types: new Backbone.Collection(),
		items: new Backbone.Collection(),
		voices: new Backbone.Collection(),
		
		setData: function(data) {
			this.types.reset(data.actionTypes);
			this.items.reset(data.items);
			this.voices.reset(data.voices);
			this.reset(data.actions);
		},
		
		// Sets the associated API resource that Actions will be assigned to:
		// Parses out the object's foreign key from the API resource.
		load: function(uri) {
			this.reset();
			this.resourceId = parseInt(uri.replace(/.*\/(.+?)\/$/g, '$1'), 10);
			this.resourceURI = uri;
			this.fetch(this.RESET);
		},
		
		comparator: function(model) {
			return model.get('action_type');
		},
		
		// Finds the first available item that is not already in use:
		getDefaultItem: function() {
			var selectedItems = this.pluck('related_item');
			return this.items.find(function(item) {
				return !_.contains(selectedItems, item.id);
			});
		},
		
		// Gets a base fieldset for new models:
		// may be overridden in sub-classes to extend fields.
		getNewModelData: function() {
			var defaultType = this.types.where({is_custom: true})[0] || this.types.at(0);
			return {
				content_object: this.resourceURI,
				action_type: defaultType.get('id')
			};
		},
		
		// HACK: request objects based on resource ID.
		// This *should* be requesting based on resource URI,
		// however Tastypie (API) seems to have issues filtering generic foreign keys.
		// Instead we'll request on resource id with no results limit,
		// and then filter out the relevant resources client-side.
		getRequestData: function(method) {
			return {
				object_id: this.resourceId,
				format: 'json',
				limit: 0
			};
		},
		
		// HACK: filter out unrelated resources that don't match the resource URI.
		// Circumvents Tastypie (API) issues with filtering on generic foreign keys.
		parse: function(response) {
			this.hasData = true;
			return _.filter(response.objects, function(model) {
				return model.content_object === this.resourceURI;
			}, this);
		}
	});
	
	return new ActionModelList();
});