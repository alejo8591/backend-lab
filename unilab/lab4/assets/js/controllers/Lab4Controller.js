/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4')
.controller('Lab4Controller', function($scope, $http){
    'use strict';
    $http.get('http://127.0.0.1:3636/data').success(function(response){

        console.log(angular.fromJson(response));

        $scope.data = response;


    });
});