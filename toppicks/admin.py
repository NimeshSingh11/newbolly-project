from django.contrib import admin
from .models import  Topcom
from .models import  Toprom
from .models import  Topthrill
# Register your models here.




class TopcomAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25

class TopromAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25

class TopthrillAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	list_per_page = 25		
	


admin.site.register(Topcom, TopcomAdmin)
admin.site.register(Toprom, TopromAdmin)
admin.site.register(Topthrill, TopthrillAdmin)
