from __future__ import unicode_literals


from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    notes = models.TextField(default="Enter notes")

    def __str__(self):
        return self.name


class Pregnancy(models.Model):
    client = models.ForeignKey(Client, related_name="pregnancies")
    due_date = models.DateField()
    week_care_commences = models.IntegerField()
    notes = models.TextField(default="Enter notes")

    def __str__(self):
        return self.client.name


class PregnancyEvent(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, related_name="pregnancy_events")
    title = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title


#
#
# class Event():
#     type foreign key to EventType
#     client
#     notes
#
#
# class EventType():
#     title
#     when
#     description

