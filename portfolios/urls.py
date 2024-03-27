from django.urls import path

from . import views

urlpatterns = [
    path('', views.PortfoliosView.as_view(), name='portfolios'),
    path('<slug:slug>/', views.PortfolioDetails.as_view(), name='portfolio-detail'),
]
