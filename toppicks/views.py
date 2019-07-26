from django.shortcuts import render,get_object_or_404


from bolly.models import Action
from bolly.models import Comedy
from bolly.models import Romance
from bolly.models import Thriller
from bolly.models import Toppicks
from .models import Topcom
from .models import Toprom
from .models import Topthrill
 

def action(request):
	action = Action.objects.all()

	return render(request,'top-picks/Action.html',{'action':action})

	


def detailact(request, detailact_id):
	detailact = get_object_or_404(Toppicks, pk=detailact_id)
	context = {
	'detailact':detailact
	}
	

	return render(request,'top-picks/detail.html',context)		


	

def comedy(request):
	comedy = Comedy.objects.all()
	return render(request,'top-picks/Comedy.html',{'comedy':comedy})	

def detailcom(request, detailcom_id):
	detailcom = get_object_or_404(Topcom, pk=detailcom_id)
	context = {
	'detailcom':detailcom
	}
	

	return render(request,'top-picks/detailcom.html',context)	

def romance(request):
	rom = Romance.objects.all()
	return render(request,'top-picks/Romance.html',{'rom':rom})	

def detailrom(request, detailrom_id):
	detailrom = get_object_or_404(Toprom, pk=detailrom_id)
	context = {
	'detailrom':detailrom
	}
	

	return render(request,'top-picks/detailrom.html',context)	

def thriller(request):
	th = Thriller.objects.all()
	return render(request,'top-picks/Thriller.html',{'th':th})

def detailthrill(request, detailthrill_id):
	detailthrill = get_object_or_404(Topthrill, pk=detailthrill_id)
	context = {
	'detailthrill':detailthrill
	}
	

	return render(request,'top-picks/detailthrill.html',context)	

