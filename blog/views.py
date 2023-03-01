from django.shortcuts import render, get_object_or_404
from .models import BlogModel
# Create your views here.

# сторінка блогу
def blog_home(request):
    post_list = BlogModel.objects.all()
    post_count = post_list.count()
    return render(request, 'blog/blog_home.html', {'post_list': post_list, 'post_count': post_count})

# відкриває окремий пост
def post_detail(request, post_id):
    # pk - primary key (database)
    post = get_object_or_404(BlogModel, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
