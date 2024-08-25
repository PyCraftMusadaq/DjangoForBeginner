from typing import Any
from django.shortcuts import render
from django.http import Http404
from .models import Post 
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
# Create your views here.

class PostList(ListView):
    model = Post 
    template_name = "blog/index.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    # def get_context_data(self,*args,**kwargs):
    #     try:
    #         return super().get_context_data(*args,**kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super().get_context_data(*args,**kwargs)
    def paginate_queryset(self, queryset, page_size):
        try:
            return super().paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super().paginate_queryset(queryset,page_size)


class MyDetailView(DetailView):
    model = Post 
    template_name = "blog/detail.html"
    