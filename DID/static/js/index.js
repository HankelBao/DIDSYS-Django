$("#login-button").click(function(){
    scorer_username = $("#login-username").val();
    scorer_password = $("#login-password").val();
    $.ajax({
        url:"scorerboard.html",
        data:{"username":scorer_username, "password":scorer_password},
        success:function(result){
            $("#modal-title").html("Welcome, Inspector");
            $("#modal-content").html(result);
        }
    });
});