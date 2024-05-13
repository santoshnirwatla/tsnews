from django.urls import path
from . import  views

urlpatterns =[
    path('indexnews/',views.indexnews_info),
    path('movies/',views.movienews_info),
    path('politics/',views.political_info),
    path('sports/',views.sports_info),
    
]