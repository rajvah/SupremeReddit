from django.shortcuts import render

# Create your views here.
def r2appView(request):
    return render(request, 'pages.html')