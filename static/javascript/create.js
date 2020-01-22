// $(document).ready(() => {


//     $("#submit_btn").click(() => {
//         let csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
//         let data ={date:$("#date_input").val(), time:$("#select1").val()}
//         console.log(data)
//           $.ajax({
//             type: "POST",
//             url: "ajax/time",
//             data: {
//               time: $("#time").val(),
//               username: $("#username"),
//               csrfmiddlewaretoken: csrfmiddlewaretoken
//             },
//             dataType: "json",
//             success: function() {

//             }
//           });
//     });
// });