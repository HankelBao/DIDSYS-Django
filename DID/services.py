from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
import datetime
import calendar
from enum import Enum


class scoreboard:
    def get_table(date_required):
        scoreboard_table = []
        for clas in Clas.objects.all():
            items = {}
            items['Class'] = clas.name
            for subject in Subject.objects.all():
                recordQ = Record.objects.filter(
                    date=date_required, subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        words = str(record.score)
                        if record.reason:
                            words += " (" + record.reason + ")"
                        items[subject.name] = words
                else:
                    items[subject.name] = "Not Scored Yet"
            scoreboard_table.append(items)
        return scoreboard_table

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
                        words = str(record.score)
                        if record.reason:
                            words += " (" + record.reason + ")"
                        items.append(words)
                else:
                    items.append("Not Scored Yet")
            scoreboard_body.append(items)
        return scoreboard_body


class scoreranking:

    def get_day_ranking_header(type):
        if type == 0:
            items = ["#", "Class Name", "Total Score of Today"]
        elif type == 1:
            items = ["#", "Class Name", "Total Score of This Week"]
        elif type == 2:
            items = ["#", "Class Name", "Total Score of This Month"]
        else:
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

    def get_3_day_ranking_table():
        clases = Clas.objects.all().order_by('-day_total')[:3]
        i = 0
        ranking_table = []
        for clas in clases:
            i += 1
            items = {}
            items['Rank'] = str(i)
            items['Class Name'] = clas.name
            items['Total Score Today'] = clas.day_total
            ranking_table.append(items)
        return ranking_table

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

    def get_4_scoremoments_table():
        records = Record.objects.all().order_by("-datetime")[:4]
        items = []
        for record in records:
            item = {}
            item['Date'] = str(record.date)
            item['Scorer'] = record.scorer.name
            item['Subject'] = record.subject.name
            item['Score'] = record.score
            item['Reason'] = record.reason
            item['Score Time'] = str(record.datetime)
            items.append(item)
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
                date__range=(datetime.datetime(now.year, now.month, 1), datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])), clas=clas)
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
                        if record.reason:
                            keys['reason'] = record.reason
                        else:
                            keys['reason'] = 'NULL'
                else:
                    keys['score'] = 'NULL'
                    keys['reason'] = 'NULL'
                keys['index'] = index
                items.append(keys)
            scoreboard_body.append(items)
        return scoreboard_body

    def update_scores(scorer, scores, scores_reason, scorer_date=datetime.date.today()):
        i = 0
        for clas in scorer.clases.all():
            for subject in scorer.subjects.all():
                i += 1
                recordQ = Record.objects.filter(
                    date=scorer_date, subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        if scores[i]:
                            record.score = scores[i]
                            # if scores_reason[i]:
                            record.reason = scores_reason[i]
                            record.save()
                        else:
                            record.delete()
                else:
                    if scores[i]:
                        if scores_reason[i]:
                            Record.objects.create(date=scorer_date, datetime=datetime.datetime.now(),
                                                  clas=clas, subject=subject, scorer=scorer, score=scores[i], reason=scores_reason[i])
                        else:
                            Record.objects.create(date=scorer_date, datetime=datetime.datetime.now(),
                                                  clas=clas, subject=subject, scorer=scorer, score=scores[i])
        scorezone.update_class_day_total()
        scorezone.update_class_month_total()
        scorezone.update_class_week_total()
        scorezone.update_class_semester_total()
