from django.urls import path
from . import views


urlpatterns = [

	
	
	path('Action/', views.action ,name='action'),
	path('Action/<int:detailact_id>/', views.detailact ,name='detailact'),
    path('Comedy/', views.comedy ,name='comedy'),
    path('Comedy/<int:detailcom_id>/', views.detailcom ,name='detailcom'),

    path('Romance', views.romance ,name='romance'),
    path('Romance/<int:detailrom_id>/', views.detailrom ,name='detailrom'),
    path('Thriller', views.thriller ,name='thriller'),
    path('Thriller/<int:detailthrill_id>/', views.detailthrill ,name='detailthrill'),
	
]