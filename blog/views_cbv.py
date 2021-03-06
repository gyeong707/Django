from .models import Post
from django import forms
from django.views.generic import DeleteView, ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


post_new = CreateView.as_view(model=Post, fields='__all__')
post_list = ListView.as_view(model=Post, paginate_by=10)
post_detail = DetailView.as_view(model=Post)
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
