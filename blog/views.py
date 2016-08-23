from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):  # request: the template path and the variables to render the given template
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts', posts})