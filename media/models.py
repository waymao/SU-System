from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name + " on " + str(self.date)


class Student(models.Model):
    name = models.CharField(max_length=100)
    grad_year = models.IntegerField(default=0)
    class_in = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    qq = models.CharField(max_length=20)
    email = models.CharField(max_length=40)


class EventPhotographerAssigned(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    assigned_photographer = models.CharField(max_length=200)


class EventFileUpload(models.Model):
    assignation = models.ForeignKey(EventPhotographerAssigned, on_delete=models.CASCADE)
    file_description = models.CharField(max_length=400)


class Feedback(models.Model):
    assignation = models.ForeignKey(EventPhotographerAssigned, on_delete=models.CASCADE)
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    content = models.CharField(max_length=1000)
# Create your models here.
