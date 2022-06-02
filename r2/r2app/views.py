import time

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .test_fields import TestFields
# from .db_wrapper import *

TEST_COUNT = 1000

# Create your views here.
def r2appView(request):
    # all_posts = Post.objects.all()
    # return render(request, 'pages.html',
    # {'all_posts': all_posts})
    return render(request, 'pages.html')


def readPostView(request):

    direct = True if request.POST['direct'] == 1 else False
    directText = "DIRECT" if direct else "WRAPPER"

    start_time = time.time()
    print(f'READING 1000 POSTS ({directText}) START: {start_time}')
    
    posts = Post.objects.len(1000)
    for p in posts:
        print("ID: ")
        print(p.id)
        print("Created At: ")
        print(p.created_at)

    print(f'READING 1000 POSTS TIME ELAPSED: {time.time() - start_time}')

    return HttpResponseRedirect('/r2app/')


def createPostView(request):

    direct = True if request.POST['direct'] == 1 else False
    directText = "DIRECT" if direct else "WRAPPER"
    
    start_time = time.time()
    print(f'CREATING 1000 POSTS ({directText}) START: {start_time}')

    for x in range(TEST_COUNT):
        new_post = Post(name="Post " + x,
                        description="Description " + x,
                        content=TestFields.char_field(),
                        upvote_count=TestFields.int_field(),
                        downvote_count=TestFields.int_field())
        new_post.save()

    print(f'CREATING 1000 POSTS TIME ELAPSED: {time.time() - start_time}')

    return HttpResponseRedirect('/r2app/')


def updatePostView(request, i):
    direct = True if request.POST['direct'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')


def deletePostView(request, i):
    direct = True if request.POST['direct'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')


def searchPostView(request, i):
    direct = True if request.POST['direct'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')
