"""demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views, hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello.hello, name='hello'),
    path('demo01/', views.dropdemo, name='dragdrop'),
    path('demo02/', views.freedraw, name='canvas01'),
    path('demo03/', views.proofread, name='typo'),
    path('demo04/', views.summarize, name='textsum'),
    path('demo05/', views.talk_do, name='talk'),
]
