"""r2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from r2app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('r2app/', r2appView),
    path('readThing/', readThingView, name = "read_thing"),
    path('createThing/', createThingView, name = "create_thing"),
    path('updateThing/', updateThingView, name = "update_thing"),
    path('deleteThing/', deleteThingView, name = "delete_thing"),
    path('searchThing/', searchThingView, name = "search_thing"),
]
