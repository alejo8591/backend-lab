<?php
class Product{
    public static function find($arr){
        global $db;
        
        if($arr['id']){
            $st = $db->prepare("SELECT * FROM products WHERE id=:id");
        }
        elseif($arr['category']){
            $st = $db->prepare("SELECT * FROM products WHERE category=:category");
        }
        else{
             throw new Exception("Unsupported property!");
        }
        $st->execute($arr);
        
        return $st->fetchAll(PDO::FETCH_CLASS, "Product");
    }
}
/*The return values of both find methods are arrays with instances
 *of the class. We could possibly return an array of generic objects
 *(or an array of arrays) in the find method, but creating specific
 *instances will allow us to automatically style each object using
 *the appropriate template in the views folder (the ones that start
 *with an underscore)
*/
?>