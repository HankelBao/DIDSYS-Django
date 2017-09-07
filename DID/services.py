from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
import datetime
from enum import Enum


class scoreboard:
    def get_table_header():
        subjects = Subject.objects.all()
        scoreboard_head = [""]
        for subject in subjects:
            scoreboard_head.append(subject.name)
        return scoreboard_head

    def get_table_body(date_required):
        scoreboard_body = []
        for clas in Clas.objects.all():
            items = [clas.name]
            for subject in Subject.objects.all():
                recordQ = Record.objects.filter(
                    date=date_required, subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        items.append(record.score)
                else:
                    items.append("Not Scored Yet")
            scoreboard_body.append(items)
        return scoreboard_body


class scoreranking:
    def get_day_ranking_header():
        items = ["#", "Class Name", "Total Score of Today"]
        return items

    def get_week_ranking_header():
        items = ["#", "Class Name", "Total Score of This Week"]
        return items

    def get_month_ranking_header():
        items = ["#", "Class Name", "Total Score of This Month"]
        return items

    def get_semester_ranking_header():
        items = ["#", "Class Name", "Total Score of This Semester"]
        return items

    def get_3_day_ranking_body():
        clases = Clas.objects.all().order_by('-day_total')[:3]
        i = 0
        ranking_body = []
        for clas in clases:
            i += 1
            items = [str(i), clas.name, clas.day_total]
            ranking_body.append(items)
        return ranking_body

    def get_3_ranking_body(type):
        if type == 0:
            clases = Clas.objects.all().order_by('-semister_total')[:3]
        elif type == 1:
            clases = Clas.objects.all().order_by('-week_total')[:3]
        elif type == 2:
            clases = Clas.objects.all().order_by('-month_total')[:3]
        else:
            clases = Clas.objects.all().order_by('-semister_total')[:3]

        ranking_body = []
        i = 0
        for clas in clases:
            i += 1
            if type == 0:
                items = [str(i), clas.name, clas.day_total]
            elif type == 1:
                items = [str(i), clas.name, clas.week_total]
            elif type == 2:
                items = [str(i), clas.name, clas.month_total]
            else:
                items = [str(i), clas.name, clas.semister_total]

            ranking_body.append(items)
        return ranking_body


class scoremoments:
    def print_record_info(record):
        return_info = " [ " + str(record.datetime) + " ] " + record.scorer.name + " scored " + str(record.score) + "      for " +\
            record.clas.name + " " + record.subject.name + \
            " for " + str(record.date)
        return return_info

    def get_4_scoremoments():
        records = Record.objects.all().order_by("-datetime")[:4]
        items = []
        for record in records:
            items.append(scoremoments.print_record_info(record))
        return items


class scorezone:
    class check_account_return(Enum):
        wrong_password = 0
        wrong_username = 1

    def check_account(username, password):
        scorers = Scorer.objects.all()
        for scorer in scorers:
            if scorer.name == username:
                if scorer.password == password:
                    return scorer
                else:
                    return scorezone.check_account_return.wrong_password
        return scorezone.check_account_return.wrong_username

    def update_class_day_total():
        clases = Clas.objects.all()
        for clas in clases:
            day_total = 0
            recordQ = Record.objects.filter(
                date=datetime.date.today(), clas=clas)
            if recordQ:
                for record in recordQ:
                    day_total += record.score
            clas.day_total = day_total
            clas.save()

    def update_class_week_total():
        clases = Clas.objects.all()
        now = datetime.datetime.now()
        for clas in clases:
            week_total = 0
            recordQ = Record.objects.filter(
                date__range=(now - datetime.timedelta(days=now.weekday()), now + datetime.timedelta(days=6 - now.weekday())), clas=clas)
            if recordQ:
                for record in recordQ:
                    week_total += record.score
            clas.week_total = week_total
            clas.save()

    def update_class_month_total():
        clases = Clas.objects.all()
        now = datetime.datetime.now()
        for clas in clases:
            month_total = 0
            recordQ = Record.objects.filter(
                date__range=(datetime.datetime(now.year, now.month, 1), datetime.datetime(now.year, now.month + 1, 1) - datetime.timedelta(days=1)), clas=clas)
            if recordQ:
                for record in recordQ:
                    month_total += record.score
            clas.month_total = month_total
            clas.save()

    def update_class_semester_total():
        clases = Clas.objects.all()
        for clas in clases:
            semester_total = 0
            recordQ = Record.objects.filter(clas=clas)
            if recordQ:
                for record in recordQ:
                    semester_total += record.score
            clas.semister_total = semester_total
            clas.save()

    def load_scoreboard_head(scorer):
        items = [""]
        for subject in scorer.subjects.all():
            items.append(subject.name)
        return items

    def load_scoreboard_body(scorer):
        scoreboard_body = []
        index = 0
        for clas in scorer.clases.all():
            items = [clas.name]
            for subject in scorer.subjects.all():
                keys = {}
                index += 1
                recordQ = Record.objects.filter(
                    date=datetime.date.today(), subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        keys['score'] = record.score
                else:
                    keys['score'] = 'NULL'
                keys['index'] = index
                items.append(keys)
            scoreboard_body.append(items)
        return scoreboard_body

    def update_scores(scorer, scores):
        i = 0
        for clas in scorer.clases.all():
            for subject in scorer.subjects.all():
                i += 1
                recordQ = Record.objects.filter(
                    date=datetime.date.today(), subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        if scores[i]:
                            record.score = scores[i]
                            record.save()
                        else:
                            record.delete()
                else:
                    if scores[i]:
                        Record.objects.create(date=datetime.date.today(), datetime=datetime.datetime.now(),
                                              clas=clas, subject=subject, scorer=scorer, score=scores[i])
        scorezone.update_class_day_total()
        scorezone.update_class_month_total()
        scorezone.update_class_week_total()
        scorezone.update_class_semester_total()
