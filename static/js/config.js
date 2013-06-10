requirejs.config({
    baseUrl: '/static/js/',
	urlArgs: 'bust='+ (new Date().getTime()),
    paths: {
        backbone: 'libs/backbone',
        jquery: 'libs/jquery',
        underscore: 'libs/underscore'
    }
});