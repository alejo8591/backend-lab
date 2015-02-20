$('#likes').click(function(){
    var product_id;
    product_id = $(this).attr('data-product-id');
    $.ajax({
      type: 'POST',
      url: '/order/product/like/',
      data: {product_id: product_id}
    }).done(function(data){
      $('#like_count').html(data);
      $('#likes').hide();
    }).fail(function(error){
      console.log(error);
    });
});
