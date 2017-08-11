from django.shortcuts import render
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
from . import services
import datetime


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
    content = {}
    content['n'] = 'Hello World!'
    return render(request, 'DID/scorerboard.html', content)
