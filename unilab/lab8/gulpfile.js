/*
* Dependencias
*/
var gulp = require('gulp'),
	cssmin = require('gulp-cssmin'),
    rename = require('gulp-rename'),
    concatCss = require('gulp-concat-css');


gulp.task('concat-css', function(){
    return gulp.src(['source/css/normalize.css', 'source/css/skeleton.css', 'source/css/styles.css'])
        .pipe(concatCss('bundle.css'))
        .pipe(gulp.dest('source/css/'));
});

gulp.task('minify-css', ['concat-css'], function(){
  return gulp.src('source/css/bundle.min.css')
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('dist/'));
});