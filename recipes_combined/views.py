from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Recipe, Favorite
from django.core.paginator import Paginator
from bson.objectid import ObjectId
from .forms import CommentForm

def recipes_list(request):
    category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    recipe_kind = request.GET.get('recipe_kind', '')
    query = {}
    if category:
        query['title__icontains'] = category
    if search_query:
        query['title__icontains'] = search_query
    if recipe_kind:
        query['recipe_kind'] = recipe_kind
    recipes = Recipe.objects.filter(**query)
    paginator = Paginator(recipes, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    no_recipes = page_obj.paginator.count == 0
    for recipe in page_obj.object_list:
        recipe.recipe_id = str(recipe._id)
        recipe.is_favorited = (request.user.is_authenticated and Favorite.objects.filter(user=request.user, recipe=recipe).exists())
    return render(request, 'recipes_combined/recipes_list.html',
                  {'page_obj': page_obj, 'search_query': search_query, 'category': category, 'recipe_kind': recipe_kind, 'no_recipes': no_recipes})

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(_id=ObjectId(recipe_id))
    comments = recipe.comment_set.all()
    is_favorited = (
        request.user.is_authenticated and
        Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    )
    recipe.recipe_id = str(recipe._id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            return redirect('recipes_combined:recipe_details', recipe_id=recipe_id)
    else:
        form = CommentForm()
    return render(request, 'recipes_combined/recipe_details.html', {
        'recipe': recipe,
        'comments': comments,
        'form': form,
        'is_favorited': is_favorited
    })

def toggle_favorite(request, recipe_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=403)
    try:
        recipe = Recipe.objects.get(_id=ObjectId(recipe_id))
        favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe, defaults={'recipe_type': recipe.recipe_kind})
        if not created:
            favorite.delete()
            is_favorited = False
        else:
            is_favorited = True

        return JsonResponse({'is_favorited': is_favorited})
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)