 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="UTF-8">
   <title>
     @section('title')
      Test Laravel
     @show
   </title>
   @section('head')
   <link rel="stylesheet" href="/css/master.css" media="screen" title="no title" charset="utf-8">
   @show
 </head>
 <body>
   @yield('content')
   <footer>
     @yield('footer', 'Este es el pie de pagina')
   </footer>
 </body>
 </html>
