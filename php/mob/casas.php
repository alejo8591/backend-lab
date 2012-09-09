<?php
include_once "aes.class.php";
include_once "aesctr.class.php";
$timer = microtime(true);
// $id=$_GET['id'];
$pw = isset($_POST['pw']) ? stripslashes($_POST['pw']) : '54321';
$id = isset($_POST['pt']) ? stripslashes($_POST['id']) : 'pssst ... đon’t tell anyøne!';
//$cipher = isset($_POST['cipher']) ? $_POST['cipher']: '';
//$plain = isset($_POST['plain']) ? stripslashes($_POST['plain']): '';
//$encr = isset($_POST['encr']) ? AesCtr::encrypt($pt, $pw, 256) : $cipher;
(int) $decr = isset($_POST['decr']) ? AesCtr::decrypt($_POST['cipher'], $pw, 256) : AesCtr::decrypt($id, $pw, 256);

process($decr);

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