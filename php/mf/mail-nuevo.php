<?php
$sAsunto = "Nuevo usuario registrado en Maqueta Fácil";
	$sPara   = "jimmycarbono@gmail.com,intercreativo@gmail.com,alejo8591@gmail.com";
	$mensaje = 'Nombre: '.$_POST['name'].'<br />Twitter: '.$_POST['twitter'].'<br />E-mail: '.$_POST['email'].'<br />País: '.$pais.'<br />';
	$sDe     = "registro@maquetafacil.com";


	$bHayFicheros = 0;
	$sCabeceraTexto = "";
	$sAdjuntos = "";

	if ($sDe)$sCabeceras = "From:".$sDe."\n";
	else $sCabeceras = "";
	$sCabeceras .= "MIME-version: 1.0\n";

	$sTexto .= '
		<html> 
		<head> 
		<meta charset="UTF-8" />
		   <title>'.$sAsunto.'</title> 
		</head> 
		<body> 
		<h1>Datos de la persona:</h1> 
		<p>
		'.$mensaje.'
		</p> 
		</body> 
		</html> 
	';

	if ($bHayFicheros == 0)
	{
	$bHayFicheros = 1;
	$sCabeceras .= "Content-type: multipart/mixed;";
	$sCabeceras .= "boundary=\"--_Separador-de-mensajes_--\"\n";

	$sCabeceraTexto = "----_Separador-de-mensajes_--\n";
	$sCabeceraTexto .= "Content-type: text/html;charset=UTF-8\n";
	$sCabeceraTexto .= "Content-transfer-encoding: 7BIT\n";

	$sTexto = $sCabeceraTexto.$sTexto;
	}
	if ($_FILES['compro']['size'] > 0)
	{
	$sAdjuntos .= "\n\n----_Separador-de-mensajes_--\n";
	$sAdjuntos .= "Content-type: ".$_FILES['compro']['type'].";name=\"".$_FILES['compro']['name']."\"\n";;
	$sAdjuntos .= "Content-Transfer-Encoding: BASE64\n";
	$sAdjuntos .= "Content-disposition: attachment;filename=\"".$_FILES['compro']['name']."\"\n\n";

	$oFichero = fopen($_FILES['compro']["tmp_name"], 'r');
	$sContenido = fread($oFichero, filesize($_FILES['compro']["tmp_name"]));
	$sAdjuntos .= chunk_split(base64_encode($sContenido));
	fclose($oFichero);
	}

	if ($bHayFicheros)
	$sTexto .= $sAdjuntos."\n\n----_Separador-de-mensajes_----\n";

	@mail($sPara, $sAsunto,$sTexto, $sCabeceras);

?>