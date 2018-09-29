from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	#ex: /www/send/
	path('send/<url>/', views.send, name='send')
]