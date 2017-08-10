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
    content['scoreboard'] = [
        [0 for i in range(len(subjects) + 1)] for j in range(len(clases) + 1)]
    content['scoreboard'][0][0] = '#'
    x = 0
    for subject in subjects:
        x += 1
        content['scoreboard'][0][x] = subject.name
    y = 0
    for clas in clases:
        y += 1
        content['scoreboard'][y][0] = clas.name
    #a = content['scoreboard']
    # a[0][0] = '#'
    return render(request, 'index.html', content)
# Create your views here.
