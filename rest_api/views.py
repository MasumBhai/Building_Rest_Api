from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context=context)


def error(request, anything=None): # template missing
    # baseEverywhere(request=request)
    context = {
    }
    return render(request, 'error.html', context=context)