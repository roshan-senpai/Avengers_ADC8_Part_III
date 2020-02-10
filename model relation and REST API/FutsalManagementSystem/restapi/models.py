from django.db import models

# Create your models here.
# creating objects for table in database 
class Payment(models.Model):
    team_name = models.CharField('Event Name',max_length=100)
    duration = models.IntegerField('Duration')
    charge = models.IntegerField('charge')
    bill = models.CharField('Bill', max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.team_name + " " + str(self.duration)+ " " + str(self.charge) + " " + self.bill



class Customer(models.Model):
    team_name = models.CharField('Team Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    contact = models.IntegerField('Contact ')
    customer_payment=models.ManyToManyField(Payment)
    def __str__(self):
        return str(self.id) + " " + self.team_name + " " + self.address+ " " + str(self.contact) 




class Event(models.Model):
    event_name = models.CharField('Event Name',max_length=100)
    venue = models.CharField('Venue',max_length=100)
    event_date = models.DateField('Event Date')
    manager = models.CharField('Manager Name', max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.event_name + " " + self.venue+ " " + str(self.event_date) + " " + self.manager




class Field(models.Model):
    field_name = models.CharField('Field Name',max_length=100)
    field_address = models.CharField('Field Address',max_length=100)
    field_contact = models.IntegerField('Field Contact')
    customer_field=models.ManyToManyField(Customer)
    def __str__(self):
        return str(self.id) + " " + self.field_name + " " + self.field_address+ " " + str(self.field_contact) 



class Booking(models.Model):
    duration = models.IntegerField('Duration')
    charge = models.IntegerField('charge')
    payment = models.IntegerField('Payment')
    team_name = models.CharField('Event Name',max_length=100)
    customer_booking=models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + " " + str(self.duration) + " " + str(self.charge)+ " " + str(self.payment) + " " + self.team_name


class Staff(models.Model):
    contact = models.IntegerField('Contact')
    name = models.CharField('Name',max_length=100)
    address = models.CharField('Address', max_length=100)
    staff_field=models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.contact)+  " " + self.team_name + " " + self.address

