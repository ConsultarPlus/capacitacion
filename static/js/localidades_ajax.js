$("#id_provincia").change(function () {
    var url = $("#urlsForm").attr("cargar_localidades-url");
    var provincia_id = $("#id_provincia").val();

    $.ajax({
        url: url,
        data: {'provincia': provincia_id},
        success: function (data) {
            var temp_localidad = $("#id_localidad").val();
            $("#id_localidad").html(data);
            $("#id_localidad").val(temp_localidad);
        }
    });
});