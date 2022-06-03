import time

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .test_fields import TestFields
# from .db_wrapper import *

TEST_COUNT = 1000

# Create your views here.
def r2appView(request):
    return render(request, 'pages.html')


def readThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "READ"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({view_text}) START')

    # replace with db_wrapper if WRAPPER
    things = Thing.objects.all()[:TEST_COUNT]
    for t in things:
        print(f'ID: {t.id} | Created At: {t.created_at}')

    time_elapsed = '%.2f' % ((time.time() - start_time) * 1000.00)
    print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms')

    return JsonResponse(
        {"message": TestFields.return_message(view_text, method, time_elapsed)},
        status=200)


def createThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "CREATE"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({view_text}) START')

    for x in range(TEST_COUNT):
        new_post = Thing(name="Post " + str(x),
                         description="Description " + str(x),
                         content=TestFields.char_field(),
                         upvote_count=TestFields.int_field(),
                         downvote_count=TestFields.int_field())
        new_post.save()

    time_elapsed = '%.2f' % ((time.time() - start_time) * 1000.00)
    print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms')

    return JsonResponse(
        {"message": TestFields.return_message(view_text, method, time_elapsed)},
        status=200)


def updateThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "UPDATE"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({view_text}) START')

    # replace with db_wrapper if WRAPPER
    things = Thing.objects.order_by('?')[:TEST_COUNT]
    for t in things:
        t.content = TestFields.char_field()
        t.upvote_count = TestFields.int_field()
        t.downvote_count = TestFields.int_field()
        t.save()

    time_elapsed = '%.2f' % ((time.time() - start_time) * 1000.00)
    print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms')

    return JsonResponse(
        {"message": TestFields.return_message(view_text, method, time_elapsed)},
        status=200)


def deleteThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "DELETE"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({view_text}) START')

    # replace with db_wrapper if WRAPPER
    things = Thing.objects.order_by('?')[:TEST_COUNT]
    for t in things:
        t.delete()

    time_elapsed = '%.2f' % ((time.time() - start_time) * 1000.00)
    print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms')

    return JsonResponse(
        {"message": TestFields.return_message(view_text, method, time_elapsed)},
        status=200)


def searchThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "SEARCH"

    start_time = time.time()
    print("==================")
    print(f'{method} 1000 THINGS ({view_text}) START (by upvote_count > 1000)')

    # replace with db_wrapper if WRAPPER
    things = Thing.objects.filter(upvote_count__gte=TEST_COUNT)
    for t in things:
        print(f'ID: {t.id} | Created At: {t.created_at} | Upvotes: {t.upvote_count}')

    time_elapsed = '%.2f' % ((time.time() - start_time) * 1000.00)
    print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms | TOTAL FOUND: {len(things)}')

    return JsonResponse(
        {"message": TestFields.return_message(view_text, method, time_elapsed)},
        status=200)
