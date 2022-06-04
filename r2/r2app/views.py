from django.shortcuts import render
from django.http import JsonResponse

from r2app.models.models import Thing, CassandraThing
from r2app.db.db_wrapper import DatabaseWrapper
from r2app.db.clientDemoHelper import DemoHelper
import r2app.db.db_cassandra as db_cass
import r2app.db.db_sql as db_sql

# Constants for demo purposes only
DEMO_COUNT = 1000
DEMO = DemoHelper()
WRAPPER = DatabaseWrapper()
DIRECT_MY_SQL = db_sql
DIRECT_NO_SQL = db_cass

# Create your views here.
def r2appView(request):
    return render(request, 'pages.html')

# BELOW CRUD METHODS

# They show the time elapsed as a measurement to show that DIRECT vs. WRAPPER
# does not compromise the performance while decoupling the direct database
# connectors from the original architecture.

# READ Thing objects from the database DIRECTLY or via WRAPPER
# based on the passed parameter of the GET request.
def readThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "READ"

    DEMO.start_time(method, view_text)
    # Wrapper vs. Direct storage DB call
    if wrapper:
        for x in range(DEMO_COUNT):
            t = WRAPPER.read(1)
            print(f'{method} {x} THINGS')
    else:
        for x in range(DEMO_COUNT):
            t = DIRECT_MY_SQL.getThing(1)
            ct = DIRECT_NO_SQL.getThing(1)
            print(f'{method} {x} THINGS')

    return JsonResponse({"message": DEMO.end(method, view_text)})


# CREATE Thing objects from the database DIRECTLY or via WRAPPER
# based on the passed parameter of the GET request.
# Fields are determined randomly from samples in test_fields.py
def createThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "CREATE"

    DEMO.start_time(method, view_text)
    thing = DemoHelper.generate_thing()
    # Wrapper vs. Direct storage DB call
    if wrapper:
        for x in range(DEMO_COUNT):
            t_id = WRAPPER.create(thing)
            print(
                f'{method} {x} THINGS | ID: {t_id}'
            )
    else:
        for x in range(DEMO_COUNT):
            t_id = DIRECT_MY_SQL.createThing(thing)
            ct_id = DIRECT_NO_SQL.createThing(thing)
            print(
                f'{method} {x} THINGS | ID: {t_id}'
            )

    return JsonResponse({ "message": DEMO.end(method, view_text) })


# UPDATE Thing objects from the database DIRECTLY or via WRAPPER
# based on the passed parameter of the GET request.
# First a query is made to sample random 1000 Things.
def updateThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "UPDATE"

    DEMO.start_time(method, view_text)
    thing = DemoHelper.generate_thing()
    # Wrapper vs. Direct storage DB call
    if wrapper:
        for x in range(DEMO_COUNT):
            t_id = WRAPPER.update(thing)
            print(f'{method} {x} THINGS | ID: {t_id}')
    else:
        for x in range(DEMO_COUNT):
            t_id = DIRECT_MY_SQL.updateThing(thing)
            print(f'{method} {x} THINGS | ID: {t_id}')

    return JsonResponse({ "message": DEMO.end(method, view_text) })


# DELETE Thing objects from the database DIRECTLY or via WRAPPER
# based on the passed parameter of the GET request.
# First a query is made to sample random 1000 Things.
def deleteThingView(request):

    wrapper = True if request.GET['wrapper'] == 1 else False
    view_text = "WRAPPER" if wrapper else "DIRECT"
    method = "DELETE"

    DEMO.start_time(method, view_text)
    # Wrapper vs. Direct storage DB call
    if wrapper:
        for x in range(DEMO_COUNT):
            res = WRAPPER.delete(1)
            print(f'{method} {x} THINGS | DELETED?: {res}')
    else:
        for x in range(DEMO_COUNT):
            sql_res = DIRECT_MY_SQL.deleteThing(1)
            cass_res = DIRECT_NO_SQL.deleteThing(1)
            print(f'{method} {x} THINGS | DELETED?: {sql_res and cass_res}')

    return JsonResponse({ "message": DEMO.end(method, view_text) })
