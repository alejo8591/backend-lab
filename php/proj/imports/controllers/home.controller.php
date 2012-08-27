<?php
class HomeController{
    public function handleRequest(){
        $content = Category::find();
        render('home', array(
            'title' => 'Welcome to the jungle',
            'content' => $content
                             ));
    }
}
?>