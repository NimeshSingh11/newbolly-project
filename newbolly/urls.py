
from django.contrib import admin
from django.urls import path,include
from bolly import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('',views.home,name='home'),

    path('LatestRelease/',include('bolly.urls')),
    path('Top-picks/',include('toppicks.urls')),
    
    
    path('grossers/huncrore', views.huncrore ,name='huncrore'),
	path('grossers/biggestfilmsyearly', views.biggestfilmsyearly ,name='biggestfilmsyearly'),
    path('grossers/highestopeningweekend', views.highestopeningweekend ,name='highestopeningweekend'),
    path('grossers/biggestfilmfranchise', views.biggestfilmfranchise ,name='biggestfilmfranchise'),
    path('grossers/biggestopeningday', views.biggestopeningday ,name='biggestopeningday'),
    path('grossers/HighestGrossers', views.HighestGrosserAllTimes ,name='HighestGrossers'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
