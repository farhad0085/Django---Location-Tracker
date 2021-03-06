from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('locations/', location_list, name="location_list"),
    path('locations/create/', location_create, name="location_create"),
    
    # auth
    path('auth/', auth_views.obtain_auth_token, name="obtain_auth_token"),
]
