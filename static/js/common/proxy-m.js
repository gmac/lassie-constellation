define([
	'backbone'
], function(Backbone) {
	
	var ProxyModel = Backbone.Model.extend({
		model: null,
		
		load: function(model) {
			if (this.model) {
				this.stopListening(this.model);
			}
			
			this.model = model;
			
			if (this.model) {
				this.listenTo(this.model, 'all', this.proxyEvent);
				this.listenTo(this.model, 'delete', this.unload);
				this.trigger('select');
			}
		},
		
		unload: function() {
			this.load(null);
		},

		proxyEvent: function(eventName) {
			this.trigger(eventName);
		},
		
		edit: function() {
			this.trigger('edit', this.model);
		},
		
		cancel: function() {
			this.trigger('cancel', this.model);
		},
		
		attrs: function() {
			return this.model ? this.model.attributes : this.attributes;
		},
		
		get: function() {
			return this.model ? this.model.get.apply(this.model, arguments) : null;
		},
		
		set: function() {
			return this.model ? this.model.set.apply(this.model, arguments) : null;
		},
		
		save: function() {
			return this.model ? this.model.save.apply(this.model, arguments) : null;
		},
		
		destroy: function() {
			return this.model ? this.model.destroy.apply(this.model, arguments) : null;
		}
	});
	
	return ProxyModel;
});