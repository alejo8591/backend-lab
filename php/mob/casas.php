<?php
(int) $id=$_GET['id'];
if($id > 0){
    process($id);
}

function process($id){
    $db = mysql_connect('localhost', 'root', '3193115');
    if(!$id){
        die('Could not connect: ' . mysql_error());
    }
    elseif(!mysql_select_db('mobphp')){
        die('Could not connect: ' . mysql_error());
    }
    else{
        $result = mysql_query("SELECT * FROM casas WHERE id=".$id);
    }
        if(!$result){
            die('Could not query:' . mysql_error());
        }
        
    $row = mysql_fetch_object($result);
    $jsondata['id'] = $row->id;
    $jsondata['m2'] = $row->m2;
    $jsondata['hab'] = $row->hab;
    $jsondata['direccion'] = $row->direccion;
    
    mysql_close($db);
    
    echo json_encode($jsondata);
}
?>