from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record


class scoreboard:
    def get_table_header():
        subjects = Subject.objects.all()
        scoreboard_head = ["#"]
        for subject in subjects:
            scoreboard_head.append(subject.name)
        return scoreboard_head

    def get_table_body(date_required):
        subjects = Subject.objects.all()
        clases = Clas.objects.all()
        scoreboard_body = []
        for clas in clases:
            items = [clas.name]
            for subject in subjects:
                recordQ = Record.objects.filter(
                    date=date_required, subject=subject, clas=clas)
                if recordQ:
                    for record in recordQ:
                        items.append(record.score)
                else:
                    items.append("Not Scored Yet")
            scoreboard_body.append(items)
        return scoreboard_body
