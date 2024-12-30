from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World ! This is the home page. Welcome to Django.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is the about page. I am a Django developer.")

def contact(request):
    return HttpResponse("This is the contact page. You can contact me at my email address.")