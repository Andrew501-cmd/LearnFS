from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def documentation(request):
    return HttpResponse('v1/allList</br>')

class V1_allList():
    pass
