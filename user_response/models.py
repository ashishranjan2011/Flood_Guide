import uuid
from django.db import models
from datetime import datetime, timedelta

def default_start_time():
    now = datetime.now
    return now
    # start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    # return start if start > now else start + timedelta(days=1)

# class Something(models.Model):

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,default="")
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    no_of_person=models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=default_start_time())
    no_of_severe_person=models.IntegerField(default=0)
    req_no = models.AutoField(primary_key=True)
    pickup=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def chng_pickup(self,x):
        # if(self.pickup == 1):
        self.pickup=x
        # else:
            # self.pickup = 1
        self.save()
# "{} - {}".format(self.lat,self.lng)


class Saver(models.Model):
    name = models.CharField(max_length=100,default="")
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    is_free = models.IntegerField(default=1)
    # boat_size = models.IntegerField(default=4)
    # timestamp = models.DateTimeField(default=default_start_time())
    # no_of_severe_person=models.IntegerField(default=0)
    next_destination = models.CharField(max_length=100,default="",blank=True)
    saver_no = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    def destination(self,pk):
        self.next_destination = str(pk)
        #     self.pickup=0
        # else:
        #     self.pickup = 1
        self.save()

    def chngfree(self,x):
        self.is_free = x
        self.save()
