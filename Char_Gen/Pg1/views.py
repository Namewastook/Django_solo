from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    return render(request, "Pg1/indexPg1.html")
