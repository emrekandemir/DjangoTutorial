from django.urls import path
from . import views



urlpatterns = [
    path('url-api', views.testapi, name = 'testapi')
]