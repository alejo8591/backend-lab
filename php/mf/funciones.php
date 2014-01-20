<?php
function registra($name,$twitter,$email,$file,$pais){
	$enlace =  mysql_connect('localhost', 'maquefa_admin', 'maqueta..');
	if(!$enlace) {
	    die('No pudo conectarse: ' . mysql_error());
	}else{
		mysql_select_db('maquefa_registro') or die(mysql_error());

		$query = "INSERT INTO mf_registrados (nombre, twitter, email, foto, pais, fecha) VALUES($name','$twitter','$email','$file','$pais', CURRENT_TIMESTAMP);";			
		$q = mysql_query($query,$enlace) or die(mysql_error());
	}
	mysql_close($enlace);
}

//Función de obtención de IP (basado en la web de webhosting.info)
function getCountry($ip_address){
  //By Marc Palau (http://www.nbsp.es)
  $url = "http://ip-to-country.webhosting.info/node/view/36";
  
  $inici = "src=/flag/?type=2&cc2=";
  
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST,"POST");
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, "ip_address=$ip_address"); 
  
  ob_start();
  
  curl_exec($ch);
  curl_close($ch);
  $cache = ob_get_contents();
  ob_end_clean();
  
  $resto = strstr($cache,$inici);
  $pais = substr($resto,strlen($inici),2);
  
  return $pais;
}

function sube_com($file){
	$tamano = $file['size'];
    $tipo = $file['type'];
    $archivo = $file['name'];
   
    if ($archivo != "") {
        // guardamos el archivo a la carpeta files
        $destino =  "comprobantes/".$archivo;
        if (copy($file['tmp_name'],$destino)) {
            $status = "Archivo subido: <b>".$archivo."</b>";
        } else {
            $status = "Error al subir el archivo";
        }
    } else {
        $status = "Error al subir archivo";
    }
}
?>