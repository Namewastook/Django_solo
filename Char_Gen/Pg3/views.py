from django.shortcuts import render
from django.http import HttpResponse
from Pg1.models import Character


def index(request):
    chars = Character.objects.all()
    context = {
        "chars": chars
    }
    return render(request, "Pg3/indexPg3.html", context=context)
