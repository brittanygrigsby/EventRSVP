from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('host/', views.host_dashboard, name='host_dashboard'),
    path('new/', views.event_create, name='event_create'),
    path('<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/guests/', views.event_guests, name='event_guests'),
]
