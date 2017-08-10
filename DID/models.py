from django.db import models

# Create your models here.


class Clas(models.Model):
    name = models.TextField()
    is_service = models.BooleanField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.TextField()
    full_score = models.IntegerField()
    is_service = models.BooleanField()

    def __str__(self):
        return self.name


class Scorer(models.Model):
    name = models.TextField()
    password = models.TextField()
    subjects = models.ManyToManyField(Subject)
    clases = models.ManyToManyField(Clas)
    is_service = models.BooleanField()

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField()
    clas = models.ForeignKey(Clas)
    subject = models.ForeignKey(Subject)
    scorer = models.ForeignKey(Scorer)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)
