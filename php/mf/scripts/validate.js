$(document).ready(function(){
	$('#register').ajaxForm({
		dataType:  'json',
        beforeSubmit: validate,
        success: showResponse
    });

    function validate(formData, jqForm, options){
    	if($("#name").val().length < 15) {
			alert("¡Tu nombre completo por favor!");
        	return false;
		}else if($("#twitter").val().length < 1) {
			alert("¡Tu nombre de usuario en twitter por favor!");
        	return false;
		}else if($("#email").val().length < 1) {
			alert("¡La dirección e-mail es obligatoria!");
        	return false;
		}else if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1) {
			alert("¡La dirección parece incorrecta!");
        	return false;
        }
    	$('#loading').html('Enviando...').show();
    }

    function showResponse(data, responseText, statusText, xhr, $form)  { 
    	$('#regist').html('<h3>'+ data.message+'</h3>');
        $("#name").val("");
        $("#twitter").val("");
        $("#email").val("");
        $("#compro").val("");
	}

	$("#compro").change(function(){
	    var val = $(this).val();
	    switch(val.substring(val.lastIndexOf('.') + 1).toLowerCase()){
	        case 'gif': case 'jpeg': case 'jpg': case 'png':
	        	var byteSize = $(this)[0].files[0].size;
		        if ( byteSize > 2097152) {
					byteSize = Math.round(byteSize *.001 * 100) * .01;
 					alert('¡Tu imagen supera los 2MB!');
				}
	            break;
	        default:
	            $(this).val('');
	            alert("¡No es una imagen!");
	            break;
	    }
    });
});