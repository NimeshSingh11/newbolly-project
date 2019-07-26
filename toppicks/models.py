from django.db import models

# Create your models here.


class Topcom(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	rating = models.CharField(max_length=10)
	Dir = models.CharField(max_length=200)
	cast = models.CharField(max_length=500)
	

	def __str__(self):
		return self.title
		

class Toprom(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	rating = models.CharField(max_length=10)
	Dir = models.CharField(max_length=200)
	cast = models.CharField(max_length=500)
	

	def __str__(self):
		return self.title		

class Topthrill(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	rating = models.CharField(max_length=10)
	Dir = models.CharField(max_length=200)
	cast = models.CharField(max_length=500)
	

	def __str__(self):
		return self.title		