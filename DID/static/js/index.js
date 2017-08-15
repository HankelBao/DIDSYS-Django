function login() {
    scorer_username = $("#login_username").val();
    scorer_password = $("#login_password").val();
    $.ajax({
        type:"POST",
        url:"ajax/get-scorerboard",
        data:{"username":scorer_username, "password":scorer_password},
        success:function(result){
            $("#modal_content").html(result);
        }
    });
}

function score_submit() {
    items_counter = $("#items_counter").val();
    var items = new Array();
    for (var i = 1; i <= items_counter; i++) {
        items[i] = $("#"+i).val();
    }
    $.ajax({
        type:"POST",
        traditional:true,
        url:"ajax/score-submit.html",
        data:{
            "scores":items,
            "username":scorer_username,
            "password":scorer_password
        },
        success:function(result){
            $("#modal_content").html(result);
        }
    });
}

function update_scoreboard()  {
    $.getJSON("ajax/get-scoreboard", function(result) {
        $("#scoreboard_header").empty();
        $.each(result.scoreboard_head, function(i, value) {
            line = "<th>" + value + "</th>";
            $("#scoreboard_header").append(line);
        })
        $("#scoreboard_body").empty();
        $.each(result.scoreboard_body, function(i, value) {
            $("#scoreboard_body").append("<tr>");
            $.each(value, function(i, item) {
                line = "<td>" + item + "</td>";
                $("#scoreboard_body").append(line);
            })
            $("#scoreboard_body").append("</tr>");
        })
    })
}
