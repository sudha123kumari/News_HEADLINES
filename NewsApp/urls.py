from django.urls import path

from NewsApp import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('technology/', views.tech, name='tech'),
    path('business/', views.business, name='business'),
    path('health/',views.health,name='health'),
    path('science/',views.science,name='science'),
    path('sports/',views.sports,name='sports'),
    path('entertainment/',views.entertainment,name='entertainment'),

]