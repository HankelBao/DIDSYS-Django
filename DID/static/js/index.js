var app = new Vue({
    el: '#rootNode',
    data: {
        scoreboard_data: new Array(),
        scoreranking_data: new Array(),
        scoremoments_data: new Array(),
        scoreboard_modal_data: new Array(),
        scoreranking_modal_data: new Array(),
        scoremoments_modal_data: new Array(),
    }
})
Vue.component('item-table', {
    name: 'item-table',
    props: {
        table_title: String,
        table_data: Array,
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
    <b-col>\
        <\
    </b-col>\
  </b-row>\
  </b-container>'
})

$(document).ready(function () {
    $.getJSON("ajax/get-scoreboard", function (result) {
        app.scoreboard_data = result;
    })
    $.getJSON("ajax/get-scoreranking", function (result) {
        app.scoreranking_data = result;
    })
    $.getJSON("ajax/get-scoremoments", function (result) {
        app.scoremoments_data = result;
    })
})