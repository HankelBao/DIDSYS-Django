from django.shortcuts import render
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
import datetime


def index(request):
    content = {}
    subjects = Subject.objects.all()
    clases = Clas.objects.all()

    content['scoreboard_head'] = ["#"]
    for subject in subjects:
        content['scoreboard_head'].append(subject.name)

    content['scoreboard_body'] = []
    for clas in clases:
        items = [clas.name]
        for subject in subjects:
            recordQ = Record.objects.filter(
                date=datetime.date.today(), subject=subject, clas=clas)
            if recordQ:
                for record in recordQ:
                    items.append(record.score)
            else:
                items.append("Not Scored Yet")
        content['scoreboard_body'].append(items)

    return render(request, 'DID/index.html', content)
# Create your views here.
