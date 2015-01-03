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
	return View::make('hello');
});

Route::get('users', function()
{
	return "Hello Dex!";
});

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
