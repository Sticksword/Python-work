from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from myblogapp.models import Post


def my_view(request):
    posts = Post.objects.all()
    post_body_list = [post.body for post in posts]
    return render_to_response('blogtemplate.html',
                             {'post_list': post_body_list})