/* The API controller
   Exports 3 methods:
   * post - Creates a new thread
   * list - Returns a list of threads
   * show - Displays a thread and its posts
*/
 
 // connect to Mongo when the app initializes
var mongoose = require('mongoose');
var db = mongoose.createConnection('mongodb://127.0.0.1:27017/testapp');

var threadSchema = require('../models/thread');
var postSchema = require('../models/post');
console.log(postSchema);
var Thread = db.model('Thread', threadSchema);
var Post = db.model('Post', postSchema);

exports.post = function(req, res) {
    new Thread({title: req.body.title, author: req.body.author}).save();
}
 
exports.list = function(req, res) {
  Thread.find(function(err, threads) {
  	console.log(threads);
    res.send(threads);
  });
}
 
// first locates a thread by title, then locates the replies by thread ID.
exports.show = (function(req, res) {
    Thread.findOne({title: req.params.title}, function(error, thread) {
        var posts = Post.find({thread: thread._id}, function(error, posts) {
          res.send([{thread: thread, posts: posts}]);
        });
    })
});