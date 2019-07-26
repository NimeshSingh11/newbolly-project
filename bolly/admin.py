from django.contrib import admin
from .models import Movie
from .models import Story
from .models import BiggestFilmYearly
from .models import  HighestOpeningWeek
from .models import  TopFilmFranchise
from .models import  huncr  
from .models import  TopDay 
from .models import  Action
from .models import  Romance
from .models import  Comedy
from .models import  Thriller
from .models import  HighestGrossers 
from .models import  Toppicks

# Register your models here.

class ActionAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25
	
admin.site.register(Action, ActionAdmin)

class ToppicksAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25

class ComedyAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25
	
class RomanceAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25
	
class ThrillerAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25

admin.site.register(Toppicks,ToppicksAdmin)

admin.site.register(HighestGrossers)

admin.site.register(Movie)

admin.site.register(Story)


admin.site.register(BiggestFilmYearly)

admin.site.register(HighestOpeningWeek)

admin.site.register(TopFilmFranchise)

admin.site.register(huncr)

admin.site.register(TopDay)



admin.site.register(Comedy,ComedyAdmin)

admin.site.register(Romance,RomanceAdmin)

admin.site.register(Thriller,ThrillerAdmin)


	
	

