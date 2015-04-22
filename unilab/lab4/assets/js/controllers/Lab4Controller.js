/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4.controllers', ['lab4.services'])
.controller('Lab4Controller', function($scope, data){
    'use strict';
    data.query(function(data){
       $scope.data = data;
    });
});