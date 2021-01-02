from django.urls import path
from . import views

urlpatterns = [
	path('results/public',views.publicKey,name="publicKey"),
	path('results/private',views.privateKey,name="privateKey"),
	path('results/',views.results,name="results"),
	
]