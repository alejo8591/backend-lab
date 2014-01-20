var http = require('http');
var path = require('path');
http.createServer(function (request, response){
	var pages = [
		{route: '', output: 'omnia sunt communia'},
		{route: 'about', output: 'communia sent'},
		{route: 'another page', output: function()
		{
			return 'Here\'s'+this.route;
		}},
	];
	var lookup = path.basename(decodeURI(request.url));
	pages.forEach(function(page){
		if(page.route === lookup){
			response.writeHead(200, {'Content-Type':'text/html'});
			response.end(typeof page.output === 'function'
				? page.output():page.output);
		}
		});
		if(!response.finished){
				response.writeHead(404);
				response.end('Page Not Found!');
			}
}).listen(3333);