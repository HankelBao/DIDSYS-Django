$("#login_button").click(function(){
    scorer_username = $("#login_username").val();
    scorer_password = $("#login_password").val();
    $.ajax({
        url:"scorerboard.html",
        data:{"username":scorer_username, "password":scorer_password},
        success:function(result){
            $("#modal-title").html("Welcome, Inspector");
            $("#modal-content").html(result);
        }
    });
});

$("#score_submit_button").click(function(){
    items_counter = $("#items_counter").val();
    var items = new Array();
    for (var i = 1; i <= items_counter; i++) {
        items[i] = $("#"+i.toString()).val();
    }
    $.ajax({
        traditional:true,
        url:"scorerboard_submit.html",
        data:{
            "scores":items,
        },
        success:function(result){
            $("#modal-title").html("Result");
            $("#modal-content").html(result);
        }
    });    
})