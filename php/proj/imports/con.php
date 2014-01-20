<?php
try{
	$db = new PDO(
		"mysql:host=$db_host;port=$db_port;dbname=$db_name;charset=UTF-8",
		$db_name,
		$db_pass
		);
	$db->query("SET NAMES 'utf8'");
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e){
	error_log($e->getMessage());
	die("A database error was encountrered");
}
?>