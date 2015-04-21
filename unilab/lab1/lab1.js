/**
 * Created by alejo8591 on 21/04/15.
 */
var http = require('http');

var server = http.createServer(function(req, res){

	res.writeHead(200, {"Content-Type" : "text/plain"});
	res.end("Hello Unipiloto\n");
});

server.listen(3333);