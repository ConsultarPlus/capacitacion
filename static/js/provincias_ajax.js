$("#id_pais").change(function () {
    var url = $("#urlsForm").attr("cargar_provincias-url");
    var pais_id = $("#id_pais").val();

    $.ajax({
        url: url,
        data: {'pais': pais_id},
        success: function (data) {
            var temp_provincia = $("#id_provincia").val();
            $("#id_provincia").html(data);
            $("#id_provincia").val(temp_provincia);
        }
    });
});
$(document).ready(function () {
    var url = $("#urlsForm").attr("cargar_provincias-url");
    var pais_id = $("#id_pais").val();

    $.ajax({
        url: url,
        data: {'pais': pais_id},
        success: function (data) {
            var temp_provincia = $("#id_provincia").val();
            $("#id_provincia").html(data);
            $("#id_provincia").val(temp_provincia);
        }
    });
});