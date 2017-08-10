from django.shortcuts import render
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record


def index(request):
    content = {}
    subjects = Subject.objects.all()
    clases = Clas.objects.all()

    content['scoreboard_size_x'] = len(subjects)
    content['scoreboard_size_y'] = len(clases)

    content['scoreboard_head'] = []
    content['scoreboard_head'].append("#")
    for subject in subjects:
        content['scoreboard_head'].append(subject.name)

    content['scoreboard_body'] = []
    for clas in clases:
        items = []
        items.append(clas.name)
        for subject in subjects:
            items.append("0")
        content['scoreboard_body'].append(items)

    return render(request, 'index.html', content)
# Create your views here.
