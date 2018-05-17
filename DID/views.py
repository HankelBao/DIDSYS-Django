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

@csrf_exempt
def index(request):
    content = {}
    content['scoreboard_head'] = services.scoreboard.get_table_header()
    return render(request, 'DID/index.html', content)


@csrf_exempt
def get_index(request):
    content = {}
    content['scoreboard_body'] = services.scoreboard.get_table_body(
        datetime.date.today())
    content['scoreranking_body'] = services.scoreranking.get_3_day_ranking_body()
    content['scoremoments'] = services.scoremoments.get_4_scoremoments()
    return HttpResponse(json.dumps(content), content_type="application/json")


@csrf_exempt
def scorerboard(request):
    content = {}
    username = request.POST['username']
    password = request.POST['password']
    return_status = services.scorezone.check_account(username, password)
    if return_status == services.scorezone.check_account_return.wrong_username:
        content['entered'] = False
        content['message'] = "Sorry. The account you entered doesn't exist."
        return render(request, 'ajax/scorerboard.html', content)
    if return_status == services.scorezone.check_account_return.wrong_password:
        content['entered'] = False
        content['message'] = "Sorry. The password you entered is incorrect."
        return render(request, 'ajax/scorerboard.html', content)

    content['entered'] = True
    scorer = return_status
    if scorer.admin:
        content['scorer_admin'] = True
        content['scorer_admin_date'] = str(datetime.date.today())
    content['scorer_name'] = scorer.name
    content["scoreboard_head"] = services.scorezone.load_scoreboard_head(
        scorer)
    content["scoreboard_body"] = services.scorezone.load_scoreboard_body(
        scorer)
    content["scoreboard_size"] = len(
        scorer.subjects.all()) * len(scorer.clases.all())
    return render(request, 'ajax/scorerboard.html', content)


@csrf_exempt
def scorerboard_submit(request):
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
        return render(request, 'ajax/scorerboard_submit.html')
    else:
        return HttpResponse("Hackers are not allowed here!")


@csrf_exempt
def get_scoreboard(request):
    return HttpResponse(json.dumps(services.scoreboard.get_table(datetime.date.today())), content_type="application/json")


@csrf_exempt
def get_scoreranking(request):
    return HttpResponse(json.dumps(services.scoreranking.get_3_day_ranking_table()), content_type="application/json")


@csrf_exempt
def get_scoremoments(request):
    return HttpResponse(json.dumps(services.scoremoments.get_4_scoremoments_table()), content_type="application/json")


@csrf_exempt
def more_on_scoreboard(request):
    content = {}
    content['date'] = request.GET['date']
    content['scoreboard_head'] = services.scoreboard.get_table_header()
    content['scoreboard_body'] = services.scoreboard.get_table_body(
        content['date'])
    return render(request, 'ajax/more_on_scoreboard.html', content)


@csrf_exempt
def more_on_scoreranking(request):
    unit_type = int(request.GET['count_unit'])

    content = {}
    if unit_type == 0:
        content['count_unit'] = "Daily"
    elif unit_type == 1:
        content['count_unit'] = "Weekly"
    elif unit_type == 2:
        content['count_unit'] = "Monthly"
    else:
        content['count_unit'] = "Semester"
    content['scoreranking_head'] = services.scoreranking.get_day_ranking_header(
        unit_type)
    content['scoreranking_body'] = services.scoreranking.get_3_ranking_body(
        unit_type)
    return render(request, 'ajax/more_on_scoreranking.html', content)

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
