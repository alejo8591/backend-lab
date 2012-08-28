var getdetails = function(id){
    $.ajax({
          data: "id="+id,
          type: "GET",
          dataType: "json",
          url: "casas.php",
          success: function(data){
            restults(data);
         }
    }); 
 };
 
var restults = function(data){
    $("div.info").html("").show();
    $("div.info").append("ID: "+data.id);
    $("div.info").append("M2: "+data.m2);
    $("div.info").append("Habitats: "+data.hab);
    $("div.info").append("Localizacion: "+data.direccion);
}