<?php
$dato = $_GET['parametro'];
$dato2 = $_GET['parametro2'];
if($dato=="valor"){
    process($dato);
}
function process($dato){
    $resultado = "hola";
    if($resultado_satisfactorio){
        $jsondata['mensaje'] = "bien";
        $jsondata['resultado'] = "resultado";
    } else{
        $jsondata['mensaje'] = "bien";
    }
    echo json_encode($jsondata);
}
?>