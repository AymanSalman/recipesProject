from django.shortcuts import render


def favorites(request,user_id):
    return render(request, 'favorites/favorites_page.html')