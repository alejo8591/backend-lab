var socket = io.connect("http://192.166.1.106:3536");
    	socket.on('news', function (data) {
    		console.log(data);
    		socket.emit('my other event', { my: 'data' });
  		});