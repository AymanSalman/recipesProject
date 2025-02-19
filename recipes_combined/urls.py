from django.urls import path
from . import views

app_name = 'recipes_combined'

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('<str:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('<str:recipe_id>/details/', views.recipe_details, name='recipe_details_with_path'),
    path('<str:recipe_id>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
]