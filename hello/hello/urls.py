"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views  # Assuming home views are in the 'home' app

admin.site.site_header = "JobSerach Admin"
admin.site.site_title = "JobSerach Admin Portal"
admin.site.index_title = "Welcome to JobSearch"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Login page as the first page
    path('index/', views.index, name='index'), 
        path("about",views.about,name='about'),
    path("services",views.services,name='services'), # Home page after login
  # Explicit login route
    path('logout/', views.logout_view, name='logout'),  # Logout route
    path('contact/', views.contact_view, name='contact'),
]
