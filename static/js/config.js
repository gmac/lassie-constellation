requirejs.config({
    baseUrl: '/static/js/',
	urlArgs: 'bust='+ (new Date().getTime()),
    paths: {
        backbone: 'libs/backbone',
        jquery: 'libs/jquery',
        underscore: 'libs/underscore'
    },
	shim: {
		backbone: {
			deps: ['jquery', 'underscore'],
			exports: 'Backbone'
		},
		underscore: {
			exports: '_'
		}
	}
});