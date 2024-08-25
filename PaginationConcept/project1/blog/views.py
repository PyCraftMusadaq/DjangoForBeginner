from django.shortcuts import render
from .models import Post 
from django.core.paginator import Paginator
# Create your views here.
def post_list(request):
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(object_list=all_posts,per_page=3,orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"blog/index.html",context={'page_obj':page_obj})
