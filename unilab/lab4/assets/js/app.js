/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4', ['ngRoute'])
.config(function($routeProvider){

    'use strict';
    $routeProvider
        .when('/', {
            templateUrl: 'js/templates/home.html'
        })
        .when('/data', {
            controller: 'Lab4Controller',
            templateUrl: 'js/templates/home.html'
        })
        .otherwise({
            redirectTo: '/'
        });
});