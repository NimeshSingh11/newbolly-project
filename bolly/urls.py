from django.urls import path
from . import views


urlpatterns = [

	path('reviews/', views.abc, name='abc'),
	path('htstory/', views.hotstory, name='hotstory'),
	path('reviews/<int:bbc_id>/', views.bbc, name='bbc'),
	path('htstory/<int:bp_id>/', views.bp, name='bp'),
	
	
]