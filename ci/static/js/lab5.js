$(document).ready(function(){
	$('#getAll').on('click', function(event){
		$.ajax({
			url: '/items/ajax/',
			type: "GET",
			datatype: 'json',
			success: function(data){
				data = $.parseJSON(data);
				for(var i = 0; i < data.length; i++) {
					$.each(data[i].fields, function(key, value){
						$('#resultAll').append('<span>Server Response: <strong>' + key + ' :' + value + '</strong></span><br />');
					});
				};
			},
			error : function(xhr,errmsg,err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});
	});

	$('#searchItem').on('click', function(event){
		$.ajax({
			url: '/items/ajax/' + $('#searchItemValue').val(),
			type: "GET",
			datatype: 'json',
			success: function(data){
				data = $.parseJSON(data);
				for(var i = 0; i < data.length; i++) {
					$.each(data[i].fields, function(key, value){
						$('#resultOne').append('<span>Server Response: <strong>' + key + ' :' + value + '</strong></span><br />');
					});
				};
			},
			error : function(xhr,errmsg,err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});
	});
});