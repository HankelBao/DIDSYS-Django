function login(){
    scorer_username = $("#login_username").val();
    scorer_password = $("#login_password").val();
    $.ajax({
        type:"POST",
        url:"ajax/get-scorerboard",
        data:{"username":scorer_username, "password":scorer_password},
        success:function(result){
            $("#modal-content").html(result);
        }
    });
}

function score_submit(){
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
            $("#modal-content").html(result);
        }
    });
}

function more_on_scoreboard() {
    $.ajax({
        url:"more_on_scoreboard.html",
        success:function(result){
            $("#modal-content").html(result);
        }
    });  
}