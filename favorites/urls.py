from django.urls import path
from .views import favorites

app_name = 'favorites'

urlpatterns = [
    path('<str:user_id>/', favorites, name='favorites_page'),
]