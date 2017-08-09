from django.db import models

# Create your models here.


class Clas(models.Model):
    name = models.TextField()
    is_service = models.BooleanField()


class Subject(models.Model):
    name = models.TextField()
    full_score = models.IntegerField()
    is_service = models.BooleanField()


class Scorer(models.Model):
    name = models.TextField()
    subjects = models.ManyToManyField(Subject)
    clases = models.ManyToManyField(Clas)
    is_service = models.BooleanField()


class Record(models.Model):
    datetime = models.DateTimeField()
    clas = models.ForeignKey(Clas)
    subject = models.ForeignKey(Subject)
    scorer = models.ForeignKey(Scorer)
