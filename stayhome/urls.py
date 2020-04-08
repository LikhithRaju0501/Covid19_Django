from django.urls import path 
from .  import views



urlpatterns = [
    path('patients/', views.patients , name="patients" ),
    path('details/', views.details , name="details" ),
    path('state_wise/', views.home , name="home" ),
    path('', views.total , name="total" ),
    path('stats', views.stats , name="stats" ),
    path('for_stats', views.for_stats , name="for_stats" ),

]