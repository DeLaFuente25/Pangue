from django.shortcuts import render
from . import views 

def home(request):
    return render(
        request,
        "base/index.html",
    )
