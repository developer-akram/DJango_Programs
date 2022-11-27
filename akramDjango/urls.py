"""akramDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('add.urls')),
    path('sub/', include('sub.urls')),
    path('mul/', include('mul.urls')),
    path('div/', include('div.urls')),
    path('fact/', include('fact.urls')),
    path('fibo/', include('fibo.urls')),
    path('hello/', include('hello.urls')),
    path('marksheet/', include('marksheet.urls')),
    path('pagechange/', include('pagechange.urls')),
    path('mysite/', include('mysite.urls')),
    path('siteone/', include('siteone.urls')),
    path('sitetwo/', include('sitetwo.urls')),
    path('sitethree/', include('sitethree.urls')),
    path('mical/', include('mical.urls')),
    path('database/', include('database.urls')),
    path('website/', include('website.urls')),
    path('trydata/', include('trydata.urls')),
    path('psite/', include('psite.urls')),
    path('polls/', include('polls.urls')),
    path('feedback/', include('feedback.urls')),
    path('check/', include('check.urls')),
    path('cookies/', include('cookies.urls')),
    path('cookiesNew/', include('cookiesNew.urls')),
    path('cookiesOld/', include('cookiesOld.urls')),
    path('classView/', include('classView.urls')),
    path('allclassview/', include('allclassview.urls')),
    path('addapp/', include('addapp.urls')),
    path('autocrud/', include('autocrud.urls')),
]
