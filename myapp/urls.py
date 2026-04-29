from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('map/', views.map_view, name='map'),
    path('panic/', views.panic_incident, name='panic'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dispatcher/', views.dispatcher, name='dispatcher'),
    path('map-data/', views.incident_data, name='map_data'), 

]