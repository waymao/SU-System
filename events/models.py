from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    hash = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    is_private = models.BooleanField()
    time = models.DateTimeField()
    publish_date = models.DateTimeField('date published')
    description = models.TextField(max_length=2000)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " at " + str(self.time)


class AttendeeInfo(models.Model):
    event_ref = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    ApprovalStatus = models.Case()
# Approved, not approved, waitlist, not_viewed
    Attend_type = models.Case()
# Participant, judge, audience, staff, admin

    def __str__(self):
        return self.attendee + " attending " + self.event_ref + " as the " + self.Attend_type
