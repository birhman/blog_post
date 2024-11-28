from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('new/', views.BlogCreateView.as_view(), name='post_create'),
    path('posts/', views.BlogListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/edit/', views.BlogEditView.as_view(), name='post_edit'),

]