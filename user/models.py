from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Contacts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12,)
    city = models.CharField(max_length = 100)
    email = models.EmailField()


    def __str__(self):
        return self.name
    
class Grps(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gname = models.CharField(max_length = 100)
    contacts = models.ManyToManyField(Contacts)
    def __str__(self):
        return self.gname
