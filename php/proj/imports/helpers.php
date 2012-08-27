<?php
function render($template, $vars = array()){
    extract($vars);
    
    if(is_array($template)){
        // include a partial view 
        foreach($template as $t){
            // create name of the object's class
            $cl = strtolower(get_class($t));
            $$cl = $t;            
            include "views/_$cl.php";
        }
    }
    else{
        include "views/$template.php";
    }
}
?>