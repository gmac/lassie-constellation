define([
	'backbone',
	'underscore',
	'common/proxy-m'
], function(Backbone, _, ProxyModel) {
	
	var ActionModelList = Backbone.Collection.extend({
		url: '/api/v1/action/',
		
		// Fill these in using .setResource();
		resourceId: 0,
		resourceURI: '/api/v1/xxx/x/',
		
		// Sets the associated API resource that Actions will be assigned to:
		// Parses out the object's foreign key from the API resource.
		setResource: function(uri) {
			this.resourceId = parseInt(uri.replace(/.*\/(.+?)\/$/g, '$1'), 10);
			this.resourceURI = uri;
		},
		
		initialize: function() {
			this.selected = new ProxyModel();
			this.listenTo(this, 'reset sync', this.setup);
		},
		
		// Setup once after initial load:
		// Create a default Action (if none available),
		// and then select the first record.
		setup: function() {
			this.stopListening(this);
			if (!this.length) this.create();
			this.select(0);
		},
		
		// HACK: request objects based on resource ID.
		// This *should* be requesting based on resource URI,
		// however Tastypie (API) seems to have issues filtering generic foreign keys.
		// Instead we'll request on resource id with no results limit,
		// and then filter out the relevant resources client-side.
		sync: function(method, model, options) {
			options.data = options.data || {};
			options.data.format = 'json';
			options.data.limit = 0;
			options.data.object_id = this.resourceId;
			Backbone.sync(method, model, options);
		},
		
		// HACK: filter out unrelated resources that don't match the resource URI.
		// Circumvents Tastypie (API) issues with filtering on generic foreign keys.
		parse: function(response) {
			return _.filter(response.objects, function(model) {
				return model.content_object === this.resourceURI;
			}, this);
		},
		
		create: function() {
			Backbone.Collection.prototype.create.call(this, {
				content_object: this.resourceURI,
				index: this.length
			});
		},
		
		select: function(model) {
			if (_.isString(model)) model = this.get(model);
			else if (_.isNumber(model)) model = this.at(model);
			
			if (model instanceof Backbone.Model) {
				this.selected.load(model);
			}
		}
	});
	
	return new ActionModelList();
});