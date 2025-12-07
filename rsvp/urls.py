from django.urls import path
from . import views

app_name = "rsvp"

urlpatterns = [
    path('', views.rsvp_home, name='rsvp'),
    path('about/', views.about, name='about'),    
    path('contact/', views.contact, name='contact'),
    path('<int:event_id>/', views.rsvp_code, name='rsvp_code'),
    path('guest/<str:token>/', views.rsvp_guest, name='rsvp_guest'),
    path('confirm/<str:token>/', views.rsvp_confirm, name='rsvp_confirm'),
]
