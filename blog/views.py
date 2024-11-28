from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Blog

def homepage(request):
    return render(request, 'blog/homepage.html')

class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ['title', 'content'] 
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:post_list')

class BlogListView(generic.ListView):
    model = Blog
    template_name='blog/blog_list.html'
    context_object_name = 'posts'

class BlogEditView(generic.UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content']
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')
