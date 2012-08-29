<?php
class Category{
    public static function find($arr = array()){
        global $db;
        
        if(empty($arr)){
            $st = $db->prepare("SELECT * FROM categories");
        }
        elseif($arr['id']){
            $st = $db->prepare("SELECT * FROM categories WHERE id=:id");
        }
        else{
            throw new Exception("Unsupported property!");
        }
        // This will execute the query, binding the $arr
        // values as query parameters
        $st->execute($arr);
        // Returns an array of Category objects:
        /*
         *the fetchAll method passing it the PDO::FETCH_CLASS constant.
         *What this does, is to loop though all the result rows,
         *and create a new object of the Category class.
         *The columns of each row will be added as public properties
         *to the object.
         */
        // Returns an array of Category objects:
	return $st->fetchAll(PDO::FETCH_CLASS, "Category");
    }
}
?>