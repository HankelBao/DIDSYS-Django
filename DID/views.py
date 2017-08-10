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

    content['scoreboard_head'] = services.scoreboard.get_table_header()
    content['scoreboard_body'] = services.scoreboard.get_table_body(
        datetime.date.today())

    return render(request, 'DID/index.html', content)
