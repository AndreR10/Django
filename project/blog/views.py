from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        "author": "André Ramos",
        "title": "Blog post 1",
        "content": "Blabla",
        "date_posted": "November 10, 2020",
    },
    {
        "author": "Inês Serra",
        "title": "Blog post 2",
        "content": "Hahahah",
        "date_posted": "November 8, 2020",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
