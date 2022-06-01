from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def r2appView(request):
    all_posts = Post.objects.all()
    return render(request, 'pages.html',
    {'all_posts': all_posts})

def addPostView(request):
    x = request.POST['name']
    new_post = Post(name = x)
    new_post.save()
    return HttpResponseRedirect('/r2app/')