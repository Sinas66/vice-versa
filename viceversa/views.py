from django.shortcuts import render


def index(req):
    return render(req, "index.html", {"title": "Vice Versa"})


def reverse(req):
    user_text = req.GET["user_text"]
    words_len = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(req, "reverse.html", {"reversed": reversed_text, "user_text": user_text, "words_len": words_len})
