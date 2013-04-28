var express = require('express');
var app = express();

var mongoose = require('mongoose');
var db = mongoose.createConnection('mongodb://127.0.0.1:27017/testapp');

 
app.configure(function(){
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
});
 
// set up the RESTful API, handler methods are defined in api.js
var api = require('./controllers/api');
app.post('/thread', api.post);
app.get('/thread/:title.:format?', api.show);
app.get('/threadlist', api.list);
 
app.listen(3000);
console.log("Express server listening on port 3000");