from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from . import services

from .models import Scorer
from .models import Clas
from .models import Subject
from .models import Record


def json_cors_response(data):
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    response["Access-Control-Allow-Credentials"] = 'true'
    return response


def json_cors_failed():
    return json_cors_response({'status': 'failed'})


def json_cors_succeed():
    return json_cors_response({'status': 'succeed'})


def scoreboard_get_by_date(request):
    date = request.GET['date']
    content = {}
    content['data'] = services.scoreboard.get_table(date)
    return json_cors_response(content)


def scorerank_get_by_type(request):
    rank_type = request.GET['type']
    content = {}
    content['data'] = services.scoreranking.get_ranking_table(rank_type, 10)
    return json_cors_response(content)


def scoremoments_query(request):
    query_params = {}
    if 'class' in request.GET:
        dclasses = Clas.objects.filter(name=request.GET['class'])
        query_params['clas'] = dclasses[0]
    if 'subject' in request.GET:
        subjects = Subject.objects.filter(name=request.GET['subject'])
        query_params['subject'] = subjects[0]
    if 'scorer' in request.GET:
        scorers = Scorer.objects.filter(name=request.GET['scorer'])
        query_params['scorer'] = scorers[0]
    if 'loss_only' in request.GET:
        query_params['score__lt'] = 10
    records = Record.objects.filter(**query_params).order_by("-datetime")[:20]
    items = []
    for record in records:
        item = services.scoremoments.create_moment_item(record)
        items.append(item)
    return json_cors_response(items)


@csrf_exempt
def scorer_login(request):
    if 'username' not in request.POST or 'password' not in request.POST:
        return json_cors_failed()

    username = request.POST['username']
    password = request.POST['password']

    scorers = Scorer.objects.filter(name=username, password=password)
    if not scorers:
        return json_cors_failed()
    request.session['userName'] = scorers[0].name
    return json_cors_succeed()


def scorer_get_session(request):
    if 'userName' not in request.session:
        return json_cors_failed()
    username = request.session['userName']
    scorers = Scorer.objects.filter(name=username)
    if not scorers:
        return json_cors_failed()

    scorer = scorers[0]

    subject_names = []
    for subject in scorer.subjects.all():
        subject_names.append(subject.name)

    class_names = []
    for clas in scorer.clases.all():
        class_names.append(clas.name)

    return json_cors_response({
        'status': 'succeed',
        'name': username,
        'admin': scorer.admin,
        'subjects': subject_names,
        'classes': class_names
    })


def scorer_session_del(request):
    request.session.clear()
    return json_cors_succeed()


def scorer_get_scores(request):
    scorer_name = request.session['userName']
    scorer = Scorer.objects.filter(name=scorer_name)[0]
    content = {}
    content['scorerboard_head'] = \
        services.scorezone.load_scoreboard_head(scorer)
    content['scorerboard_size'] = \
        len(scorer.subjects.all()) * len(scorer.clases.all())
    if scorer.admin:
        date = request.GET['date']
        content['scorerboard_body'] = \
            services.scorezone.load_scoreboard_body(scorer, date)
    else:
        content['scorerboard_body'] = \
            services.scorezone.load_scoreboard_body(scorer)
    return json_cors_response(content)


@csrf_exempt
def scorer_submit_score(request):
    scores = request.POST.getlist('scores')
    score_reasons = request.POST.getlist('score_reasons')

    scorer_name = request.session['userName']
    scorer = Scorer.objects.filter(name=scorer_name)[0]

    if scorer.admin:
        date = request.POST['date']
        services.scorezone.update_scores(scorer, scores, score_reasons, date)
    else:
        services.scorezone.update_scores(scorer, scores, score_reasons, datetime.date.today())
    return json_cors_response({"status": "succeed"})


def scorer_update_totals(request):
    services.scorezone.update_class_day_total()
    services.scorezone.update_class_month_total()
    services.scorezone.update_class_week_total()
    services.scorezone.update_class_semester_total()
    return json_cors_succeed()


def scorers_get_names(request):
    scorers = Scorer.objects.all()
    scorer_names = []
    for scorer in scorers:
        scorer_names.append(scorer.name)
    return json_cors_response(scorer_names)


def classes_get_names(request):
    classes = Clas.objects.all()
    class_names = []
    for dclass in classes:
        class_names.append(dclass.name)
    return json_cors_response(class_names)


def subjects_get_names(request):
    subjects = Subject.objects.all()
    subject_names = []
    for subject in subjects:
        subject_names.append(subject.name)
    return json_cors_response(subject_names)
