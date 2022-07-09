from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('',views.index,name='MyApp'),
    path('index',views.index,name='MyApp'),
    path('about',views.about,name='About'),
    path('services',views.services,name='Services'),
    path('contact',views.contactus,name='contact'),
    path('search_result',views.search_result,name='Search-result'),
]
