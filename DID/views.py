from django.shortcuts import render
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record

def index(request):
    content = {}
    list = Subject.objects.all()

    content['scoreboard'] = [[0 for i in range(6)] for j in range(6)]
    content['scoreboard'][5][0] = '#'
    #a = content['scoreboard']
    # a[0][0] = '#'
    return render(request, 'index.html', content)
# Create your views here.
