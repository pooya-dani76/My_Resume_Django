from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.AboutMeView.as_view() , name='about-me')
]
