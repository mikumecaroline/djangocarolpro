from django.shortcuts import render, redirect
from .model import Fashions


def index_page(request):
    data = Fashions.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def login_page(request):
    return render(request, "login.html")


def edit_page(request):
    return render(request, "edit.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        trousers = request.POST.get('trousers')
        shoes = request.POST.get('shoes')
        blouses = request.POST.get('blouses')
        dresses = request.POST.get('dresses')
        handbags = request.POST.get('handbags')

        mikume= Fashions(trousers=trousers, shoes=shoes, blouses=blouses, dresses=dresses,
                         handbags=handbags)
        mikume.save()
        return redirect("")

    return render(request, "index.html")


def deleteData(request, id):
    d = Fashions.objects.get(id=id)
    d.delete()
    return redirect("")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        trousers = request.POST.get('trousers')
        shoes = request.POST.get('shoes')
        blouses = request.POST.get('blouses')
        dresses = request.POST.get('dresses')
        handbags = request.POST.get('handbags')

        update_info = Fashions.objects.get(id=id)

        update_info.trousers = trousers
        update_info.shoes = shoes
        update_info.blouses = blouses
        update_info.dresses = dresses
        update_info.handbags = handbags
        update_info.save()

        return redirect("")

    d = Fashions.objects.get(id=id)
    context = {"d": d}
    return render(request, "index.html.", context)
