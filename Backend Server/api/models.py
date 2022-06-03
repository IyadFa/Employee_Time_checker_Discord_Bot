from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255)
    _id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200, choices=(("Joined", "Joined"), ("Left", "Left")))
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time']

class Report(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    time_spent = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.name + " Report " + str(self.date_created)

class WeeklyReport(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    weekly_time = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.name + " Weekly Report " + str(self.date_created)
    