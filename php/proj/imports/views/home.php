<?php render('_header', array('title'=>$title)) ?>
<p>Yeah! App</p>
<ul data-role="list-view" data-inset="true" data-theme="c" data-dividertheme="b">
    <li data-role="list-divider">
        Choose product category
    </li>
    <?php render($content) ?>
</ul>
<?php  render('_footer') ?>