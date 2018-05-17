from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from flask_jsonpify import jsonify

import json
import datetime
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
from . import services

def json_cors_response(data):
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def scoreboard_board_get(request):
    content = {}
    content['data'] = services.scoreboard.get_table(datetime.date.today())
    return json_cors_response(content)

def scoreboard_board_get_by_date(request):
    date = request.GET['date']
    content = {}
    content['data'] = services.scoreboard.get_table(date)
    return json_cors_response(content)

def scoreboard_rank_get(request):
    content = {}
    content['data'] = services.scoreranking.get_3_day_ranking_table()
    return json_cors_response(content)

def scoreboard_rank_get_by_type(request):
    rank_type = request.GET['type']
    content = {}
    content['data'] = services.scoreranking.get_3_ranking_table(rank_type)
    return json_cors_response(content)

@csrf_exempt
def scorer_login(request):
    content = {}
    username = request.POST['username']
    password = request.POST['password']
    return_status = services.scorezone.check_account(username, password)
    if return_status == False:
        content['status'] = 0
        return json_cors_response(content)

    content['status'] = 1
    scorer = return_status
    if scorer.admin:
        content['scorer_admin'] = True
        content['scorer_admin_date'] = str(datetime.date.today())
    content['scorer_name'] = scorer.name
    content["scorerboard_head"] = services.scorezone.load_scoreboard_head(
        scorer)
    content["scorerboard_body"] = services.scorezone.load_scoreboard_body(
        scorer)
    content["scorerboard_size"] = len(
        scorer.subjects.all()) * len(scorer.clases.all())
    return json_cors_response(content)

@csrf_exempt
def scorer_submit_score(request):
    scores = request.POST.getlist('scores')
    scores_reason = request.POST.getlist('scores_reason')
    username = request.POST['username']
    password = request.POST['password']
    scorer = services.scorezone.check_account(username, password)
    if scorer:
        if scorer.admin:
            scorer_date = request.POST['scorer_date']
            services.scorezone.update_scores(scorer, scores, scores_reason, scorer_date)
        else:
            services.scorezone.update_scores(scorer, scores, scores_reason, datetime.date.today())
        return json_cors_response({"status":"succeed"})
    else:
        return json_cors_response({"status":"failed"})
