var app = new Vue({
    el: '#rootNode',
    data: {
        scoreboard_data: new Array(),
        scoreranking_data: new Array(),
        scoremoments_data: new Array(),
        scoreboard_modal_data: new Array(),
        scoreranking_modal_data: new Array(),
        scoremoments_modal_data: new Array(),
    },
    methods: {
        login: function (event) {
            scorer_username = $("#login_username").val();
            scorer_password = $("#login_password").val();
            $.ajax({
                type: "POST",
                url: "ajax/get-scorerboard",
                data: {
                    "username": scorer_username,
                    "password": scorer_password
                },
                success: function (result) {
                    $("#modal_content").html(result);
                }
            });
        },
        update_index: function (event) {
            $.getJSON("ajax/get-scoreboard", function (result) {
                app.scoreboard_data = result;
            })
            $.getJSON("ajax/get-scoreranking", function (result) {
                app.scoreranking_data = result;
            })
            $.getJSON("ajax/get-scoremoments", function (result) {
                app.scoremoments_data = result;
            })
        }
    }
})

Vue.component('item-table', {
    name: 'item-table',
    props: {
        table_title: String,
        table_data: Array,
        when_click: String,
    },
    template: '<b-container>\
    <b-row><br><br><br><br></b-row>\
    <b-row>\
      <b-col>\
        <h1 style="text-align:center">{{table_title}}</h1>\
      </b-col>\
    </b-row>\
    <b-row>\
      <b-col>\
        <b-table :items="table_data">\
        </b-table>\
      </b-col>\
    </b-row>\
    <b-row>\
    <b-col v-if="when_click">\
        <div style="text-align:right">\
        <a :onclick="when_click" data-toggle="modal" data-target="#modal"><u>More On {{table_title}} >></u></a>\
        </div>\
    </b-col>\
  </b-row>\
  </b-container>'
})

$(document).ready(function () {
    app.update_index();
})

function score_submit() {
    items_counter = $("#items_counter").val();
    var items = new Array();
    var items_reason = new Array();
    for (var i = 1; i <= items_counter; i++) {
        items[i] = $("#" + i).val();
        items_reason[i] = $("#" + i + "R").val();
    }
    $("#modal_content").html("We are busy loading data and checking your account.<br>Please wait patiently...");
    $.ajax({
        type: "POST",
        traditional: true,
        url: "ajax/score-submit.html",
        data: {
            "scores": items,
            "scores_reason": items_reason,
            "username": scorer_username,
            "password": scorer_password
        },
        success: function (result) {
            $("#modal_content").html(result);
            app.update_index();
        }
    });
}

function more_on_scoreboard_click() {
    var myDate = new Date();
    more_on_scoreboard(myDate.getFullYear() + '-' + (myDate.getMonth() + 1) + '-' + myDate.getDate());
}

function more_on_scoreboard(input_date) {
    $.ajax({
        type: "GET",
        url: "ajax/more-on-scoreboard",
        data: {
            "date": input_date
        },
        success: function (result) {
            $("#modal_content").html(result);
        }
    });
}

function more_on_scoreranking_click() {
    more_on_scoreranking(0);
}

function more_on_scoreranking(count_unit) {
    $.ajax({
        type: "GET",
        url: "ajax/more-on-scoreranking",
        data: {
            "count_unit": count_unit
        },
        success: function (result) {
            $("#modal_content").html(result);
        }
    });
}