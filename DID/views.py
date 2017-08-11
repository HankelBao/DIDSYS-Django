from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
from . import services


def index(request):
    content = {}
    subjects = Subject.objects.all()
    clases = Clas.objects.all()
    services.scorezone.update_class_day_total()
    content['scoreboard_head'] = services.scoreboard.get_table_header()
    content['scoreboard_body'] = services.scoreboard.get_table_body(
        datetime.date.today())

    content['scoreranking_head'] = services.scoreranking.get_day_ranking_header()
    content['scoreranking_body'] = services.scoreranking.get_3_day_ranking_body()

    content['scoremoments'] = services.scoremoments.get_4_scoremoments()
    return render(request, 'DID/index.html', content)


def scorerboard(request):
    username = request.GET['username']
    password = request.GET['password']
    return_status = services.scorezone.check_account(username, password)
    if return_status == services.scorezone.check_account_return.wrong_username:
        return HttpResponse("Sorry. The account you entered doesn't exist.")
    if return_status == services.scorezone.check_account_return.wrong_password:
        return HttpResponse("Sorry. The password you entered is incorrect.")

    scorer = return_status
    content = {}
    content["scoreboard_head"] = services.scorezone.load_scoreboard_head(
        scorer)
    content["scoreboard_body"] = services.scorezone.load_scoreboard_body(
        scorer)
    content["scoreboard_size"] = len(
        scorer.subjects.all()) * len(scorer.clases.all())
    return render(request, 'DID/scorerboard.html', content)


def scorerboard_submit(request):
    content = {}
    scores = request.GET.getlist('scores')
    return HttpResponse(scores)
