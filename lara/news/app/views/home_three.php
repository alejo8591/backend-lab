<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Home</title>
</head>
<body>
  <h1>Ejemplo de vista y  controlador con RESTful</h1>
  <h4>Nombre:<?php echo Session::get('name') . " " . Session::get('lastname'); ?></h4>
  <h4>Telefono: <?php echo Session::get('phone'); ?></h4>
</body>
</html>
