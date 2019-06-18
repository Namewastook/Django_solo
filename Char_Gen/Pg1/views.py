from django.shortcuts import render, redirect
from .models import Character
from random import choice
from django.http import HttpResponse


def index(request):
    return render(request, "Pg1/indexPg1.html")


def created_char(request):
    if request.method == "POST":

        new_char = Character(race=request.POST.get("race"),
                             classes=request.POST.get("classes"),
                             strength=request.POST.get("strength"),
                             dexterity=request.POST.get("dexterity"),
                             constitution=request.POST.get("constitution"),
                             intelligence=request.POST.get("intelligence"),
                             wisdom=request.POST.get("wisdom"),
                             charisma=request.POST.get("charisma"))

        checking_data = {
            "char": new_char
        }

        return render(request, "Pg2/indexPg2.html", context=checking_data)

    return redirect("verify_data")


def random_char(request):
    if request.method == "POST":

        new_char = Character(race=request.POST.get("race"),
                             classes=request.POST.get("classes"),
                             strength=request.POST.get("strength"),
                             dexterity=request.POST.get("dexterity"),
                             constitution=request.POST.get("constitution"),
                             intelligence=request.POST.get("intelligence"),
                             wisdom=request.POST.get("wisdom"),
                             charisma=request.POST.get("charisma"))

        print("Char saved")

        new_char.save()

        return redirect("verify_data")

    return redirect("verify_data")


def verify_data(request):

    verify_datas = Character(race=choice(["Dwarf", "Elf", "Half-Elf", "Half-Orc",                                            "Halfling", "Human"]),
                             classes=choice(
        ["Cleric", "Fighter", "Rogue", "Wizard"]),
        strength=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        dexterity=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        constitution=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        intelligence=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        wisdom=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        charisma=choice(
        [10, 11, 12, 13, 14, 15, 16, 17, 18]))

    checking_data = {
        "char": verify_datas
    }

    return render(request, "Pg2/indexPg2.html", context=checking_data)
