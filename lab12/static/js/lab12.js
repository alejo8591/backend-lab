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

  $('#customer_button').click(function(event){

    event.preventDefault();
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
      $('#customer_update').show();
      $('#customer_delete').show();
      localStorage.setItem('data', JSON.stringify(data));
      console.log(data);
      return false;
    }).fail(function(error){
      console.log(error);
    });
  });

  $('#customer_update').click(function(event){
    event.preventDefault();
    if($('input[type="text"]').attr('readonly') === 'readonly'){
      $('input').removeAttr('readonly');
      event.preventDefault();
    } else{
      var local = JSON.parse(localStorage.getItem('data'));

      var data = {
        "customer_name": $('#customer_name').val(),
        "customer_phone": $('#customer_phone').val(),
        "customer_address": $('#customer_address').val()
      };
      $.ajax({
        type: 'PUT',
        url: local.url,
        dataType: 'JSON',
        data: data
      }).done(function(data){
        $('#customer_form>label, #customer_form>br').hide();
        $('#customer_form>input').attr('readonly', true);
        $('#customer_form>#customer_button').hide()
        $('#customer_update').show();
        $('#customer_delete').show();
        console.log(data);
        return false;
      }).fail(function(xhr, error, displayError){
        console.log(error);
      });
      event.preventDefault();
    }
  });

  $('#customer_delete').click(function(e){
    var local = JSON.parse(localStorage.getItem('data'));
    $.ajax({
      type: 'DELETE',
      url: local.url,
      statusCode: {
        204: function(data){
          $('#customer_form').prependTo('<a href="/order/" class="button">Ir al Inicio</a>');
          $('#customer_form').hide();
        }
      }
    }).done(function(data, textStatus, jqXHR){
      // http://stackoverflow.com/questions/16219595/how-to-handle-a-204-response-in-jquery-ajax
      if (jqXHR.status == 204) {
        console.log(jqXHR.status);
        $('h1').append('<a href="/order/" class="button">Ir al Inicio</a>');
        $('#customer_form').hide();
      }
    }).fail(function(xhr, error, displayError){
      console.log(error);
    });
    event.preventDefault();
  });
});
