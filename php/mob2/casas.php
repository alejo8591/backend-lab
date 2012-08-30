<?php
include_once "aes.class.php";
include_once "aesctr.class.php";
// $timer = microtime(true);
$pw = '54321';
(int) $decr = AesCtr::decrypt($_GET['id'], $pw, 256);

process($decr);

function process($id){
    
    $db = mysql_connect('127.0.0.1', 'root', '3193115');
    if(!$id){
        die('Could no connect: ' . mysql_error());
    }
    elseif(!mysql_select_db('mobphp')){
        die('Could no connect db:' . mysql_error());
    }
    else{
        $result = mysql_query("SELECT * FROM casas WHERE id=".$id);
    }
        if(!$result){
            die('Could not query:' . mysql_error());
        }
/*
    $row = mysql_fetch_object($result);
    $jsondata['id'] = $row->id;
    $jsondata['m2'] = $row->m2;
    $jsondata['hab'] = $row->hab;
    $jsondata['direccion'] = $row->direccion;
    
    mysql_close($db);
    
    echo json_encode($jsondata);
}
*/
    $pw = '54321';
    $row = mysql_fetch_object($result);
    $jsondata['id'] = AesCtr::encrypt($row->id, $pw, 256);
    $jsondata['m2'] = AesCtr::encrypt($row->m2, $pw, 256);
    $jsondata['hab'] = AesCtr::encrypt($row->hab, $pw, 256);
    $jsondata['direccion'] = AesCtr::encrypt($row->direccion, $pw, 256);
    
    mysql_close($db);
    
    echo json_encode($jsondata);
}
?>