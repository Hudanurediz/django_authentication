from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('index/',views.index,name='index'),
    path('login/',views.logins, name='logins'),   
    path('homepage/',views.homepage, name='homepage'),
]

