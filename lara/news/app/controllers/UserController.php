<?php

class UserController extends \BaseController
{
  public function getIndex()
  {
    return "Index RESTFul";
  }

  public function getSee()
  {
    //return "See RESTFul";
    return View::make('home')->with('name', 'Laura Romero');
  }

  public function getFirstOne()
  {
    return View::make('home')->with('name', 'Alejandro Romero');
  }

  public function getViewOne()
  {
    return View::make('home_two', array(
      'name' => 'Alejandro',
      'lastname' => 'Romero',
      'phone' => '232423432423',

    ));
  }

  public function getViewTwo()
  {
    return Redirect::to('users/view-three');
  }

  public function getViewThree()
  {
    return View::make('home_two', array(
      'name' => 'Keren',
      'lastname' => 'Sarai',
      'phone' => '67676',

    ));
  }

  public function getViewFour()
  {
    return Redirect::to('users/view-five')->with(array(
      'name' => 'Keren',
      'lastname' => 'Sarai',
      'phone' => '67676',
    ));
  }

  public function getViewFive()
  {
    return View::make('home_three');
  }
}
