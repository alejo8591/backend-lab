 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="UTF-8">
   <title>
     @section('title')
      Test Laravel
     @show
   </title>
   <!-- Bootstrap core CSS -->
   <!-- <link href="css/bootstrap.min.css" rel="stylesheet"> -->
   {{ HTML::style('css/bootstrap.min.css') }}
   @section('head')
   <!-- Custom styles for this template -->
   {{ HTML::style('css/styles.css') }}
   @show
 </head>
 <body>
   @yield('content')
   <footer>
     @yield('footer', 'Este es el pie de pagina')
   </footer>
 </body>
 </html>
