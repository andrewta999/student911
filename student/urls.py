from django.urls import path
from . import views

urlpatterns = [
	path('', views.learning),
	path('share/', views.share),
	path('<int:number>/', views.subject),
	path('home/', views.home),
]