from django.shortcuts import render

# Create your views here.
def newAppHome(request):
    return render(request, 'newApp/index.html')