/**
 * Created by alejo8591 on 21/04/15.
 */
angular.module('lab4')
	.directive('lab4Focus', function todoFocus($timeout) {
		'use strict';

		return function (scope, elem, attrs) {
			scope.$watch(attrs.todoFocus, function (newVal) {
				if (newVal) {
					$timeout(function () {
						elem[0].focus();
					}, 0, false);
				}
			});
		};
	});
