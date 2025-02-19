from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    comments = forms.CharField(widget=forms.HiddenInput(), required=False)
    favorites = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('comments', 'favorites')