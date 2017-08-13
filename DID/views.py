from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
from . import services


@csrf_exempt
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
    username = request.POST['username']
    password = request.POST['password']
    scorer = services.scorezone.check_account(username, password)
    if scorer:
        services.scorezone.update_scores(scorer, scores)
        return render(request, 'ajax/scorerboard_submit.html')
    else:
        return HttpResponse("Hackers are not allowed here!")


def more_on_scoreboard(request):
    return render(request, 'ajax/more_on_scoreboard.html')
