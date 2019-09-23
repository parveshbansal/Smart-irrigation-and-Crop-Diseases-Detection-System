from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Godown Table
class cropdetail(models.Model):
	name= models.CharField(max_length=30)
	cropname=models.CharField(max_length=30)
	cropquantity=models.IntegerField()
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('home',)	
class irrigation(models.Model):
	status_choices=((1,'1ststage'),(2,'2ndstage'),(3,'3rdstage'),(4,'4thstage'),(5,'5thstage'))
	CropStage=models.IntegerField(choices=status_choices,default='1ststage')
class CropType(models.Model):
	status_choices=((1,'Wheat'),(2,'Ground Nuts'),(3,'Garden flowers'),(4,'Maize'),(5,'Paddy'),(6,'Potato'),(7,'pulse'),(8,'SugerCane'),(9,'coffee'))
	TypeOfCrop=models.IntegerField(choices=status_choices,default='Wheat')
class Userphone(models.Model):
	username1=models.CharField(max_length=30)
	phoneno=models.IntegerField()