from django.shortcuts import render


def index(req):
    return render(req, "index.html", {"title": "Vice Versa"})


def reverse(req):
    user_text = req.GET["user_text"]
    reversed_text = user_text[::-1]
    return render(req, "reverse.html", {"reversed": reversed_text, "user_text": user_text})
