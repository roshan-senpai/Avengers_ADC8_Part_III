from django.db import models
from django.contrib.auth.models import Permission

# creating objects for table in database 
class Event(models.Model):
    event_name = models.CharField('Event Name',max_length=100)
    venue = models.CharField('Venue',max_length=100)
    event_date = models.DateField('Event Date')
    manager = models.CharField('Manager Name', max_length=100)
    #files = models.ImageField(upload_to = 'profiles')

    def __str__(self):
        return str(self.id) + " " + self.event_name + " at " + self.venue +" "+self.event_date+ " "+ self.manager
