var express = require('express'),
    path = require('path'),
    fs = require('fs'),
    compression = require('compression'),
    morgan = require('morgan'),
    method_override = require('method-override'),
    responseTime = require('response-time'),
    serveIndex = require('serve-index'),
    busboy = require('connect-busboy'),
    error_handler = require('errorhandler');

var app = express();

var access_log_stream = fs.createWriteStream(__dirname + '/access.log',{flags: 'a'});

app.set('view cache', true);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.set('port', process.env.PORT || 3000);
// app.use(compression({threshold: 1}));
app.use(morgan('combined', {stream: access_log_stream}));
app.use(method_override('_method'));
app.use(responseTime(4));

app.use('/shared', serveIndex(
    path.join('public','shared'),
    {'icons': true}
));
app.use(express.static('public'));

app.use('/upload', busboy({immediate: true }));

app.use('/upload', function(request, response) {
    request.busboy.on('file', function(fieldname, file, filename, encoding, mimetype) {
        file.on('data', function(data){
            fs.writeFile('upload' + fieldname + filename, data);
        });
        file.on('end', function(){
            console.log('File ' + filename + ' is ended');
        });

    });
    request.busboy.on('finish', function(){
        console.log('Busboy is finished');
        response.status(201).end();
    })
});

app.delete('/purchase-orders', function(request, response){
    console.log('The DELETE route has been triggered');
    response.status(204).end();
});

app.get('/response-time', function(request, response){
    setTimeout(function(){
        response.status(200).end();
    }, 513);
});

app.get('/', function(request, response){
    response.send('Pro Express.js Middleware');
});

app.get('/compression', function(request, response){
    response.render('index');
});

app.use(error_handler());
var server = app.listen(app.get('port'), function() {
    console.log('Express server listening on port ' + server.address().port);
});