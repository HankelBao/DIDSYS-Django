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

    def get_3_day_ranking_body():
        clases = Clas.objects.all().order_by('-day_total')[:3]
        i = 0
        ranking_body = []
        for clas in clases:
            i += 1
            items = [str(i), clas.name, clas.day_total]
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
