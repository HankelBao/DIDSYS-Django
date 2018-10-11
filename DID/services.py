from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record
import datetime
import calendar


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


class scoreranking:
    def get_ranking_table(type, size):
        type_table = {
            'daily': ['day_total', 'Total Score of Today'],
            'weekly': ['week_total', 'Total Score of This Week'],
            'monthly': ['month_total', 'Total Score of This Month'],
            'semesterly': ['semister_total', 'Total Score of This Semester']
        }
        db_index = 0
        des_index = 1

        if type not in type_table:
            return

        clases = \
            Clas.objects.all().order_by('-'+type_table[type][db_index])[:size]

        ranking_table = []
        for index, clas in enumerate(clases):
            items = {}
            items['Rank'] = str(index + 1)
            items['Class Name'] = clas.name
            items[type_table[type][des_index]] = \
                clas.__getattribute__(type_table[type][db_index])

            ranking_table.append(items)
        return ranking_table


class scoremoments:
    def create_moment_item(record):
        item = {}
        item['Date'] = str(record.date)
        item['Scorer'] = record.scorer.name
        item['Class'] = record.clas.name
        item['Subject'] = record.subject.name
        item['Score'] = record.score
        item['Reason'] = record.reason
        item['Score Time'] = str(record.datetime.strftime("%H:%M, %b %d %Y"))
        return item

    def get_scoremoments_table():
        records = Record.objects.all().order_by("-datetime")[:8]
        items = []
        for record in records:
            item = scoremoments.create_moment_item(record)
            items.append(item)
        return items

    def get_scorements_table_by_class(className):
        recordQ = Clas.objects.filter(name=className)
        if recordQ:
            for record in recordQ:
                clas = record
                records = \
                    Record.objects.filter(clas=clas, score__lt=10).order_by("-datetime")[:20]
                items = []
                for record in records:
                    item = scoremoments.create_moment_item(record)
                    items.append(item)
                return items


class scorezone:
    def check_account(username, password):
        scorers = Scorer.objects.all()
        for scorer in scorers:
            if scorer.name == username:
                if scorer.password == password:
                    return scorer
                else:
                    return False
        return False

    def update_class_day_total():
        clases = Clas.objects.all()
        for clas in clases:
            day_total = 0
            recordQ = Record.objects.filter(
                date=datetime.date.today(), clas=clas)
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

    def load_scoreboard_body(scorer, date=datetime.date.today()):
        scoreboard_body = []
        index = -1 
        for clas in scorer.clases.all():
            items = [clas.name]
            for subject in scorer.subjects.all():
                keys = {}
                index += 1
                recordQ = Record.objects.filter(
                    date=date, subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        keys['score'] = record.score
                        if record.reason:
                            keys['reason'] = record.reason
                        else:
                            keys['reason'] = ""
                else:
                    keys['score'] = ""
                    keys['reason'] = ""
                keys['index'] = index
                items.append(keys)
            scoreboard_body.append(items)
        return scoreboard_body

    def update_scores(scorer, scores, scores_reason, scorer_date=datetime.date.today()):
        i = -1 
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
