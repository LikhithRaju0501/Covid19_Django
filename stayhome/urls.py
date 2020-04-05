from django.urls import path 
from .  import views



urlpatterns = [
    path('patients/', views.patients , name="patients" ),
    path('details/', views.details , name="details" ),
    path('', views.home , name="home" ),
]