$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-persona .modal-content").html("");
        $("#modal-persona").modal("show");
      },
      success: function (data) {
        $("#modal-persona .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#persona-table tbody").html(data.html_persona_lista);
          $("#modal-persona").modal("hide");
        }
        else {
          $("#modal-persona .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create persona
  $(".js-crear-persona").click(loadForm);
  $("#modal-persona").on("submit", ".js-book-create-form", saveForm);

  // Update persona
  $("#persona-table").on("click", ".js-actualizar-persona", loadForm);
  $("#modal-persona").on("submit", ".js-persona-actualizar-form", saveForm);

  // Delete persona
  $("#persona-table").on("click", ".js-eliminar-persona", loadForm);
  $("#modal-persona").on("submit", ".js-persona-eliminar-form", saveForm);
  
   $("#persona-table").on("click", ".js-detalle-persona", loadForm);
   $("#modal-persona").on("submit", ".js-persona-detalle-form", saveForm);

});
/*
$('#persona-table').DataTable({
    responsive: true,
    "language": {
      "lengthMenu": "Mostrar _MENU_ registros por pagina",
        "zeroRecords": "No se encontraron resultados en su busqueda",
        "searchPlaceholder": "Buscar registros",
        "info": "Mostrando registros de _START_ al _END_ de un total de  _TOTAL_ registros",
        "infoEmpty": "No existen registros",
        "infoFiltered": "(filtrado de un total de _MAX_ registros)",
        "search": "Buscar:",
        "paginate": {
        "first": "Primero",
            "last": "Último",
            "next": "Siguiente",
            "previous": "Anterior"
        },
    }
});
*/