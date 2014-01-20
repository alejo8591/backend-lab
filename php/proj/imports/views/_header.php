<!DOCTYPE HTML>
<html lang="es-ES">
<head>
	<meta charset="UTF-8">
	<title><?php echo formatTitle($title) ?></title>
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
	<script type="text/javascript" src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
</head>
<body>
    <div data-role="page">
	<div data-role="header" data-theme="b">
		<a href="./" data-icon="home" data-iconpos="notext" data-transition="fade">Home</a>
		<h1>
			<?php echo $title ?>
		</h1>
	</div>
        <div data-role="content">