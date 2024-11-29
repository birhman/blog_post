from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, logout_page

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    path('logout-page/', logout_page, name='logout_page'),



]
