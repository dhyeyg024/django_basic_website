from pyexpat import model
from django.db import models

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mob = models.CharField(max_length=12)
    subject = models.CharField(max_length=122)
    msg = models.TextField()
    date = models.DateField()

    def __str__(self) : # function to change the name of entry in database
        return self.name

class Component(models.Model):
    type = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    weight =  models.CharField(max_length=122)

    def __str__(self) : # function to change the name of entry in database
        return self.type

