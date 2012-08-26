var http = require('http');
http.createServer(function (request, response){
	response.writeHead(200, {'Content-Type':'text/html'});
	response.end('omnia Sunt Communia');
}).listen(3333);