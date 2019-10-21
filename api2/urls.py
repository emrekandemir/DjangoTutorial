from django.conf.urls import include
from django.urls import path
from .views import *


urlpatterns = [
    path('url-api2', homepage, name = 'testapi2')
]