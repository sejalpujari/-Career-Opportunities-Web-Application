from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact", views.contact_view, name='contact'), 
    path('login/', views.login_view, name='login'), # Changed from 'views.contact' to 'views.contact_view'

]


