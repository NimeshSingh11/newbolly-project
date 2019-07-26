from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	card_text = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	rating = models.CharField(max_length=10)
	Dir = models.CharField(max_length=200)
	cast = models.CharField(max_length=500)
	

	def __str__(self):
		return self.title

class Story(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')


	def __str__(self):
		return self.title

class BiggestFilmYearly(models.Model):
	Year = models.CharField(max_length=20)
	Name = models.CharField(max_length=200)
	Director = models.CharField(max_length=200)
	Business = models.CharField(max_length=100)

	def __str__(self):
		return self.Year

class HighestOpeningWeek(models.Model):
	Rank = models.CharField(max_length=10)
	Name = models.CharField(max_length=100)
	Release_Date = models.CharField(max_length=100)
	OpeningWeek = models.CharField(max_length=100)

	def __str__(self):
		return self.Rank		

class TopFilmFranchise(models.Model):
	Rank = models.CharField(max_length=10)
	Franchise = models.CharField(max_length=100)
	Business = models.CharField(max_length=20)
	films = models.IntegerField()
	topfilm = models.CharField(max_length=100)

	def __str__(self):
		return self.Rank

class huncr(models.Model):
	Rank = models.CharField(max_length=10)
	Movie = models.CharField(max_length=100)
	Business = models.CharField(max_length=100)
	days = models.IntegerField()

	def __str__(self):
		return self.Rank	

class TopDay(models.Model):
	Rank = models.CharField(max_length=10)
	Movie = models.CharField(max_length=100)
	day = models.CharField(max_length=10)
	

	def __str__(self):
		return self.Rank		

class Action(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	text  = models.TextField()
	

	def __str__(self):
		return self.title		

class Comedy(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	text  = models.TextField()
	

	def __str__(self):
		return self.title			

class Romance(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	text  = models.TextField()
	

	def __str__(self):
		return self.title		

class Thriller(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	text  = models.TextField()
	

	def __str__(self):
		return self.title		

class HighestGrossers(models.Model):
	Rank = models.CharField(max_length=20)
	Name = models.CharField(max_length=200)
	Director = models.CharField(max_length=200)
	Business = models.CharField(max_length=100)

	def __str__(self):
		return self.Rank		

class Toppicks(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	rating = models.CharField(max_length=10)
	Dir = models.CharField(max_length=200)
	cast = models.CharField(max_length=500)
	

	def __str__(self):
		return self.title

		

		
