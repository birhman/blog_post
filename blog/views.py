from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Apply to class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Apply to function-based views
@login_required
def homepage(request):
    return render(request, "blog/homepage.html")

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ["title", "content"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:post_list")

class BlogListView(generic.ListView):
    model = Blog
    template_name='blog/blog_list.html'
    context_object_name = 'posts'

class BlogEditView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    fields = ["title", "content"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:post_list")

class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy("blog:post_list")









