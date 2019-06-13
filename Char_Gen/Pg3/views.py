from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "Pg3/indexPg3.html")
