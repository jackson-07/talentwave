from django.db import models
from django.urls import reverse

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f'{self.first_name} {self.last_name}')


class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    city =  models.CharField(max_length=50)
    candidates = models.ManyToManyField(Record)
    
    def __str__(self): 
        return(f'{self.name}')

