from django.db import models
from item.models import Item

# Create your models here.
class ItemHistory(models.Model):
	item = models.ForeignKey(Item)
	date_on = models.DateField(auto_now_add = True)

        
	class Meta:
		unique_together = ('item','date_on')
