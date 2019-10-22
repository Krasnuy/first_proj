from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('input/', views.input),
    path('about/', views.about),
    path('guitar/', views.guitar),
    path('elguitar/', views.elguitar),
    path('cabinet/', views.cabinet),
    path('equipments/', views.equipments),
    path('keys/', views.keys),
    path('actions/', views.actions),
    path('contacts/', views.contacts)
]