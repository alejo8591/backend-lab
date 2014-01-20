<?php
	$asunto = "Gracias por registrarte - Maqueta Fácil";
	$para   = $_POST['email'];
	$de     = "registro@maquetafacil.com";


	$cabeceraTexto = "";

	if ($de)$cabeceras = "From:".$de."\n";
	else $cabeceras = "";
	$cabeceras .= "MIME-version: 1.0\n";

	$texto .= '
		<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8" />
	<title> Maqueta Facil : Cursos online de Diseño y Maquetación </title>
	<link rel="stylesheet" href="http://maquetafacil.com/mail/css/style.css" />
</head>
<body>
	<section id="contenedor">
		<header>
			<a href="http://www.maquetafacil.com"> <img src="http://maquetafacil.com/mail/images/logo.png" alt="Bienvenido" /> </a>
		</header>
		<section id="info">
			<h1>¡Gracias por Registrarte!</h1>
			<h2>Bienvenido</h2>
			<p>Felicitaciones, hemos recibido tus datos satisfactoriamente, permítenos verificar los datos de tu comprobante
				y en un lapso no mayor de 48 hrs. recibirás el código para acceder al curso.<br/>
				<br/>
				Toma en cuenta que de preferencia deberás de tener instalado <b>Adobe Photoshop CS6</b> que puedes descargar
				en la página oficial de <a href="http://www.adobe.com/cfusion/tdrc/index.cfm?product=photoshop&loc=es_es"><b>Adobe</b></a>, no te preocupes si no quieres una licencia puedes probarlo por 30 días.
				<br/><br/>Así como también <a href="http://www.sublimetext.com/2"><b>Sublime Text 2</b></a> que es multiplataforma y sobre todo muchas ganas de aprender.
				<br/><br/>
				No te olvides que la fecha del cursos son los días:
				<br><br>
				<b>- Viernes 28 de Septiembre 4:00 p.m. (-6 México)</b><br><br>
				<b>- Sábado 29 de Septiembre 12:00 p.m. (-6 México)</b><br><br>

				Esos días utilizaremos el Hashtag #maquetafacil
				<br/><br/>
				Cualquier duda o comentario escríbenos a <a href="mailto:contacto@maquetafacil.com">contacto@maquetafacil.com</a> 
				o llamanos si estás en México al teléfono:
				<br/><br/>
				<b>01 (55) 8421 3038</b> si estás en otro país solo agrega (+52) </p><br><br>
		</section>
		<footer>
			<a href="http://www.html5facil.com"> <img src="http://maquetafacil.com/mail/images/html5facil.png" alt="HTML5 Facil" /></a>
			<a href="http://www.ninjacode.tv"> <img src="http://maquetafacil.com/mail/images/ninjacodetv.png" alt="Ninja Code TV" /></a>
		</footer>
	</section>
</body>
</html>
	';


	$cabeceras .= "Content-type: multipart/mixed;";
	$cabeceras .= "boundary=\"--_Separador-de-mensajes_--\"\n";

	$cabeceraTexto = "----_Separador-de-mensajes_--\n";
	$cabeceraTexto .= "Content-type: text/html;charset=UTF-8\n";
	$cabeceraTexto .= "Content-transfer-encoding: 7BIT\n";

	$texto = $cabeceraTexto.$texto;

	@mail($para, $asunto,$texto, $cabeceras);
?>