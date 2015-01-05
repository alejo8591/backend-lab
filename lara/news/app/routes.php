<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|*/

/*
For MAC OS X:
http://stackoverflow.com/questions/13514990/laravel-4-all-routes-except-home-result-in-404-error
*/
Route::get('/', function()
{
	return View::make('login.login');
});

Route::resource('news', 'NewsController');

Route::post('news/create', function()
{
})->before('csrf');

/*Route::get('users', function()
{
	return "Hello Dex!";
});*/

Route::controller('users', 'UserController');

/*
Route::get('person/always/{name}', function($name)
{
	return "Hello " . $name;
});

Route::get('person/optional/{name?}', function($name = null)
{
	if ($name != null)
	{
		return "Hello " . $name;
	}

	else
	{
		return "Hello YOPO";
	}
});

Route::get('professor/unvalidated/{name}/{age}', function($name, $age)
{
	return "El nombre del profesor es: " . $name . " y su edad es de: " . $age;
});

/* Validated fields with `where()` method
Route::get('professor/validated/{name}/{age}', function($name, $age)
{
	return "El nombre del profesor es: " . $name . " y su edad es de: " . $age;
})->where(array('name'=>'[a-zA-Z]+', 'age'=>'[0-9]+'));

/*
Estas validaciones se replican para cada ruta que siga hacia abajo


Route::pattern('name','[a-zA-Z]+');
Route::pattern('age','[0-9]+');

Route::get('professor/validated/pattern/{name}/{age}', function($name, $age)
{
	return "El nombre del profesor es: " . $name . " y su edad es de: " . $age;
});*/

/*
Rutas especificas para utilizar con el filtro `session`


Route::get('session/create', function()
{
	Session::put('name','Alejandro');
	return "Se Crea la sesión correctamente";
});

Route::get('session/delete', function()
{
	Session::forget('name');
	return "Se Elimina la sesión correctamente";
});

Route::get('login', function()
{
	return "Ingrese al sistema";
});

/* Primera forma de utilizar el filtro `session`
Route::get('users/filter/one', array('before'=>'session', function()
{
	return "Hello Filtro Uno!";
}));

/* Segunda forma de utilizar el filtro `session`
Route::get('users/filter/two', function()
{
	return "Hello Filtro Dos!";
})->before('session');

/* Tercera forma de filtros utilizando el metodo `group()`
Route::group(array('before'=>'session'), function()
{

	Route::get('users/filter/three', array('before'=>'session', function()
	{
		return "Hello Filtro Tres!";
	}));

	/* Segunda forma de utilizar el filtro `session`
	Route::get('users/filter/four', function()
	{
		return "Hello Filtro Cuatro!";
	})->before('session');

});
*/
