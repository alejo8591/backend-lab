<?php
/*
 * This file include files
 * only used in index.php
*/
require_once "imports/config.php";
require_once "imports/con.php";
require_once "imports/helpers.php";
require_once "imports/models/product.model.php";
require_once "imports/models/category.model.php";
require_once "imports/controllers/home.controller.php";
require_once "imports/controllers/category.controller.php";

// optional

header('Cache-control: max-age=3600, public');
header('Pragma: cache');
header("Last-Modified: ".gmdate("D, d M Y H:i:s",time())." GMT");
header("Expires: " .gmdate("D, d M Y H:i:s",time()+3600)." GMT");
?>