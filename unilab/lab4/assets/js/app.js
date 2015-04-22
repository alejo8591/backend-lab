/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4', ['ngRoute'])
       .config(function($routeProvider) {

        'use strict';
		var routeConfig = {
			controller: 'Lab4Controller',
			templateUrl: 'list.html',
			resolve: {
				store: function(lab4Storage){
					// Get the correct module (API or localStorage).
					return lab4Storage.then(function(module){
						module.get(); // Fetch the todo records in the background.
						return module;
					});
				}
			}
		};

		$routeProvider
			.when('/', routeConfig)
			.when('/:status', routeConfig)
            .when('/data', routeConfig)
			.otherwise({
				redirectTo: '/'
			});
	});