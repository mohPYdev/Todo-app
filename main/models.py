from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    STATUS = (
        ('done' , 'done'),
        ('not done' , 'not done'),
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100 , null=True)
    description = models.TextField(max_length=500 , null=True)
    data_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50 , choices=STATUS , null=True)

    def __str__(self):
        return self.title

