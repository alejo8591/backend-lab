<?php
require_once "imports/main.php";
try{
   if($_GET['category']){
    $c = new CategoryController();
   }
   elseif(empty($_GET)){
    $c = new HomeController();
   }
   else throw new Exception("Wrong page!");
   $c -> handleRequest();
}
catch(Exception $e){
    // Display error using render()
    render('error', array('message'=>$e->getMessage()));
}
?>