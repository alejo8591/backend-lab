/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4', ['ngRoute', 'lab4.controllers', 'lab4.services'])
.config(function($routeProvider){

    'use strict';
    $routeProvider
        .when('/', {
            templateUrl: 'js/templates/home.html'
        })
        .when('/data', {
            controller: 'Lab4Controller',
            templateUrl: 'js/templates/data.html'
        })
        .otherwise({
            redirectTo: '/'
        });
});