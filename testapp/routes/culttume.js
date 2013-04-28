(function() {
  var User, db, mongoose, userSchema;

  mongoose = require('mongoose');

  db = mongoose.connect('mongodb://127.0.0.1:27017/culttume');

  userSchema = require('../models/user');

  User = db.model('User', userSchema);

  exports.index = function(req, res) {
    res.render('index', {
      title: 'Bienvenido a culttu.me'
    });
    return console.log('loaded index view');
  };

  exports.list = function(req, res) {
    return User.find(function(err, users) {
      console.log(users);
      return res.send(users);
    });
  };

}).call(this);
