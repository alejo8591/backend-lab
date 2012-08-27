<?php
/*
 * This file include files
 * only used in index.php
*/
require_once "config.php";
require_once "con.php";
require_once "helpers.php";
require_once "models/category.model.php";
require_once "models/product.model.php";
require_once "controllers/category.controller.php";
require_once "controllers/home.controller.php";

// optional

header('Cache-control: max-age=3600, public');
header('Pragma: cache');
header("Last-Modified: ".gmdate("D, d M Y H:i:s",time())." GMT");
header("Expires: " .gmdate("D, d M Y H:i:s",time()+3600)." GMT");
?>