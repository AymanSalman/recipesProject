from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('recipes/', include('recipes_combined.urls')),
    path('accounts/', include('accounts.urls')),
    path('about_us/', include('about_us.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('favorites/', include('favorites.urls')),
]
urlpatterns += staticfiles_urlpatterns()