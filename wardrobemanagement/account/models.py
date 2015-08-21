from django.db import models

# Create your models here.
class MyUser(models.Model):
	name = models.CharField(max_length = 50 , blank = False)
	email= models.EmailField(max_length = 254, null = False)
