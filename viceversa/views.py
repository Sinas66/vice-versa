from django.shortcuts import render


def index(req):
    return render(req, "index.html", {"title": "Vice Versa"})
