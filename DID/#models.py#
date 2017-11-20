from django.db import models

# Create your models here.


class Clas(models.Model):
    name = models.TextField()
    register_year = models.IntegerField()
    day_total = models.IntegerField(default=0)
    week_total = models.IntegerField(default=0)
    month_total = models.IntegerField(default=0)
    semister_total = models.IntegerField(default=0)
    is_service = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.TextField()
    full_score = models.IntegerField(default=10)
    is_service = models.BooleanField(default=True)
    weeky = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Scorer(models.Model):
    name = models.TextField()
    password = models.TextField()
    subjects = models.ManyToManyField(Subject)
    clases = models.ManyToManyField(Clas)
    is_service = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField()
    datetime = models.DateTimeField()
    clas = models.ForeignKey(Clas)
    subject = models.ForeignKey(Subject)
    scorer = models.ForeignKey(Scorer)
    score = models.IntegerField()
    reason = models.TextField(null=True)

    def __str__(self):
        return str(self.score)
