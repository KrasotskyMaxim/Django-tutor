from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "New Post", 'url_name': "add_post"},
    {'title': "Feedback", 'url_name': "feedback"},
    {'title': "Sign-in", 'url_name': "sign-in"},
]


# Create your views here.
def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': "Main page",
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': "About site"})


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
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': "Showing by categories",
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h2>This page not found!</h2>") 