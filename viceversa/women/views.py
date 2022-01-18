from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


# Create your views here.
def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'title': "Main page",
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': "About site"})


def add_post(request):
    return HttpResponse("<h2>New post</h2>")


def feedback(request):
    return HttpResponse("<h2>Write feedback</h2>")


def sign_in(request):
    return HttpResponse("<h2>Sign-in</h2>")


def show_post(request, post_id):
    return HttpResponse(f"<h2>Page with post_id = {post_id}</h2>")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': "Showing by categories",
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h2>This page not found!</h2>") 