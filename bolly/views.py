from django.shortcuts import render,get_object_or_404

from .models import Movie
from .models import Story
from .models import BiggestFilmYearly
from .models import HighestOpeningWeek
from .models import TopFilmFranchise
from .models import huncr  
from .models import TopDay

from .models import HighestGrossers





# Create your views here.

def home(request):
	return render(request, 'index.html')


def abc(request):
	abc = Movie.objects.all()
	context = {	
	'abc':abc
	}
	return render(request, 'Reviews.html',context)


def bbc(request, bbc_id):
	bbc = get_object_or_404(Movie, pk=bbc_id)
	context = {
	'bbc':bbc
	}
	return render(request, 'moviedetail.html',context)	

def hotstory(request):
	hotstory = Story.objects.all()
	context = {
	'hotstory':hotstory
	}
	
	return render(request,'hotstory.html',context)

def bp(request, bp_id):
	bp = get_object_or_404(Story, pk=bp_id)
	context = {
	'bp':bp
	}
	
	return render(request,'blogs.html', context)



def biggestfilmsyearly(request):
	bfy = BiggestFilmYearly.objects.all()

	return render(request,'grossers/bfy.html',{'bfy' : bfy})

def huncrore(request):
	hun = huncr.objects.all()

	return render(request,'grossers/100croreclub.html',{'hun':hun})
	

def highestgrossingalltimes(request):

	return render(request,'grossers/HGAL.html')

def highestopeningweekend(request):
	HOW = HighestOpeningWeek.objects.all()

	return render(request,'grossers/HOW.html',{'HOW':HOW})


def biggestfilmfranchise(request):
	tff = TopFilmFranchise.objects.all()

	return render(request,'grossers/TFF.html',{'tff':tff})	


def biggestopeningday(request):
	tod = TopDay.objects.all()

	return render(request,'grossers/TOD.html',{'tod':tod})	

def HighestGrosserAllTimes(request):
	hg = HighestGrossers.objects.all()

	return render(request,'grossers/HGAL.html',{'hg' : hg})

	