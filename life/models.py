from django.db import models

#class Group(models.Model):
#	established = models.DateTimeField(auto_now_add=True)
#	name = models.CharField(max_length=50)

class Kid(models.Model):
  name = models.CharField(max_length=50)
  reading_level = models.CharField(max_length=10)
  
class Report(models.Model):
  date = models.DateField("Date Created")
  summary = models.CharField(max_length=1000)
  kid = models.ForeignKey(Kid, on_delete=models.CASCADE)