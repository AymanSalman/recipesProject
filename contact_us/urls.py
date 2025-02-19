from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('thanks/', views.thanks, name='contact_us_thanks'),
]