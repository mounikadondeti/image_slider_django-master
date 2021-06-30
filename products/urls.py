from . import views
from django.urls import path

urlpatterns = [
	path('', views.Timer, name="timer"),
	path('excel/', views.Excel, name="excel"),
]