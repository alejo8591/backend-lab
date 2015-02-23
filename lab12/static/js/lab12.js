$(document).ready(function(){
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

  $('#customer_list_button').click(function(e){
    $.ajax({
      type: 'GET',
      url: '/order/customer/ajax/list/'
    }).done(function(data){
        $.each(data, function(key, value){
          console.log(value.customer_name);
          $('#customer_list').append(
            '<li><a href="/order/customer/detail/' + value.customer_slug + '/">' +
            value.customer_name + '</a></li>');
      });
    }).fail(function(xhr, error, displayError){
      console.log(error);
    });
  });

  $('#customer_button').click(function(e){
    var data;

    data = {
      "customer_name": $('#customer_name').val(),
      "customer_phone": $('#customer_phone').val(),
      "customer_address": $('#customer_address').val()
    };

    $.ajax({
      type: 'POST',
      url: '/api/v1/customer/',
      dataType: 'JSON',
      data: data
    }).done(function(data){
      $('#customer_form>label, #customer_form>br').hide();
      $('#customer_form>input').attr('readonly', true);
      $('#customer_form>#customer_button').hide()
      $('#customer_form').append('<a id="customer_update" class="button">Editar Cliente</a>');
      console.log(data);
      return false;
    }).fail(function(error){
      console.log(error);
    });
    e.preventDefault();
  });
});
