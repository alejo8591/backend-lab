var express = require('express'),
    path = require('path'),
    morgan = require('morgan'),
    consolidate = require('consolidate'),
    fs = require('fs'),
    swig = require('swig'),
    error_handler = require('errorhandler');

var app = express();
var router = express.Router();

var access_log_stream = fs.createWriteStream(__dirname + '/access.log',{flags: 'a'});

app.engine('html', consolidate.swig);
app.set('view engine', 'html');
app.set('views', path.join(__dirname, 'views'));

app.set('port', process.env.PORT || 3000);
app.use(morgan('combined', {stream: access_log_stream}));

app.use(express.static('public'));

var users = {
        'alrock': {
            'email': 'hi@alrock.co',
            'website': 'http://alrock.co',
            'blog': 'http://alrockblog.com'
        }
};

var findUserByUsername = function(username, callback){
    //perform database query that calls callback when it’s done
    // this is our fake database
    if (!users[username])
        return callback(new Error(
                'No user matching '
                + username
            )
        );
    return callback(null, users[username]);
};

/* lab6 first part */
app.get('/v1/users/:username', function(request, response, next) {
    var username = request.params.username;
    findUserByUsername(username, function(error, user) {
        if(error) return next(error);

        console.log(user);
        return response.render('index', user);
    });
});

app.get('/v1/admin/:username', function(request, response, next) {
    var username = request.params.username;
    findUserByUsername(username, function(error, user) {
        if (error) return next(error);
        return response.render('admin', user);
    });
});


/* lab6 second part */
var findUserByUsernameMiddleware = function(request, response, next){

    if(request.params.username){
        console.log(
            'Username param was is detected: ',
            request.params.username
        );

        findUserByUsername(
            request.params.username,
            function(error, user){
                if (error) return next(error);
                request.user = user;
                return next();
            }
        );
    } else {
        return next();
    }
};

app.get('/v2/users/:username',

    findUserByUsernameMiddleware,

    function(request, response, next){
        return response.render('index', request.user);
    });

app.get('/v2/admin/:username',

    findUserByUsernameMiddleware,

    function(request, response, next){
        return response.render('admin', request.user);
    });


/* lab6 third part */
app.param('v3Username', function(request, response, next, username){
    console.log(
        'Username param was is detected: ',
        username
    );

    findUserByUsername(
        username,
        function(error, user){
            if (error) return next(error);
            request.user = user;
            return next();
        }
    );
});

app.get('/v3/users/:v3Username',
    function(request, response, next){
        return response.render('index', request.user);
    }
);

app.get('/v3/admin/:v3Username',
    function(request, response, next){
        return response.render('admin', request.user);
    }
);

router.param('username', function(request, response, next, username){
    console.log(
        'Username param was is detected: ',
        username
    );

    findUserByUsername(
        username,
        function(error, user){
            if (error) return next(error);
            request.user = user;
            return next();
        }
    );
});


router.get('/users/:username',
    function(request, response, next){
        return response.render('user', request.user);
    }
);


router.get('/admin/:username',
    function(request, response, next){
        return response.render('admin', request.user);
    }
);


app.use('/v4', router);

app.use(error_handler());

var server = app.listen(app.get('port'), function() {
    console.log('Express server listening on port ' + server.address().port);
});