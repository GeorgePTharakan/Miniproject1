"""
URL configuration for mini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from miniapp import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.LandingBeforeLogin, name='LandingBeforeLogin'),
    path('Signup/', views.Signup, name='Signup'),
    
    path('Login/', views.Login, name='Login'),
    path('Profile/',views.Profile, name='Profile'),
    path('LandingAfterLogin/',views.LandingAfterLogin, name='LandingAfterLogin'),
    path('About/',views.About, name='About'),
    path('Courses/',views.Courses, name='Courses'),
    path('Pythoncourse/',views.Pythoncourse, name='Pythoncourse'),
    path('Javacourse/',views.Javacourse, name='Javacourse'),
    path('Cppcourse/',views.Cppcourse, name='Cppcourse'),
]

