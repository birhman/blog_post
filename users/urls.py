from django.urls import path
from .views import profile_view, edit_profile

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]
