from django.urls import path
from app1.views import *
app1_name='app1'
urlpatterns=[
    path('dj/',dj,name='dj')
]