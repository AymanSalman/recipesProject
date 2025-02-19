from django.conf import settings
from djongo import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    DoesNotExist = None
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=255)
    ingredients = models.JSONField()
    instructions = models.TextField()
    picture_link = models.URLField(max_length=500, blank=True, null=True)
    recipe_kind = models.CharField(max_length=50)  # 'ar', 'epi', 'fn'

    class Meta:
        db_table = "combined_recipes"  # Collection name

    def __str__(self):
        return f'Recipe: "{self.title}" ({self.recipe_kind})'

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by "{self.author}" on recipe: "{self.recipe}"'

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_type = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f'{self.user.username} favorites {self.recipe.title}'