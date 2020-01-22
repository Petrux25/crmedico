$(document).ready(() => {
  $("#add-time").click(() => {
    let csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
      type: "POST",
      url: "ajax/time",
      data: {
        time: $("#time").val(),
        username: $("#username").val(),
        csrfmiddlewaretoken: csrfmiddlewaretoken
      },
      dataType: "json",
      success: function(response) {
        $("#times").append(`<li class="list-group-item">${response.time}</li>`)
      }
    });
  });
});

