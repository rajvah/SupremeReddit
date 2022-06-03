import time

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .test_fields import TestFields
# from .db_wrapper import *

TEST_COUNT = 1000

# Create your views here.
def r2appView(request):
    # all_things = Thing.objects.all()
    # return render(request, 'pages.html',
    # {'all_things': all_things})
    return render(request, 'pages.html')


def readThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    wrapperText = "WRAPPER" if wrapper else "DIRECT"
    method = "READ"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({wrapperText}) START')

    things = Thing.objects.all()[:TEST_COUNT]
    for t in things:
        print(f'ID: {t.id} | Created At: {t.created_at}')

    print(f'{method} 1000 THINGS TIME ELAPSED: {(time.time() - start_time) * 1000.000} ms')

    return JsonResponse({ "message": TestFields.return_message(wrapperText, method) }, status = 200)


def createThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    wrapperText = "WRAPPER" if wrapper else "DIRECT"
    method = "CREATE"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({wrapperText}) START')

    for x in range(TEST_COUNT):
        new_post = Thing(name="Post " + str(x),
                        description="Description " + str(x),
                        content=TestFields.char_field(),
                        upvote_count=TestFields.int_field(),
                        downvote_count=TestFields.int_field())
        new_post.save()

    print(f'{method} 1000 THINGS TIME ELAPSED: {(time.time() - start_time) * 1000.000} ms')

    return JsonResponse({ "message": TestFields.return_message(wrapperText, method) }, status = 200)


def updateThingView(request, i):
    wrapper = True if request.GET['wrapper'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')


def deleteThingView(request, i):
    wrapper = True if request.GET['wrapper'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')


def searchThingView(request, i):
    wrapper = True if request.GET['wrapper'] == 1 else False
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/r2app/')
