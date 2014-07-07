module.exports=function(grunt){
	// Project configuration.
	grunt.initConfig({pkg:grunt.file.readJSON('package.json'),

	concat:{
		app:{
			src:['static/js/*.js'],
			dest:'static/js/app.js'},
		vendor:{
			src:['static/js/*.js'],
			dest:'build/static/js/lib.js'
		}
	},
	uglify:{
		app:{
			files:{'static/js/app.min.js':['static/js/*.js']
		}
	},
		vendor:{
			files:{
				'build/static/js/lib.min.js':['myproject/static/js/*.js']
			}
	  	}
	}

	// Task configuration goes here.
	});
	// Load plugins here.
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-sass');
	grunt.loadNpmTasks('grunt-contrib-less');
	grunt.loadNpmTasks('grunt-contrib-watch');
	
	// Register tasks here.
	grunt.registerTask('default',['concat', 'uglify']);
};
