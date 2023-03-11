from app2.views import *
from app1.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('app2_page/',app2_page,name='app2-page'),
    path('app1_page/',app1_page,name='app1_page'),
]