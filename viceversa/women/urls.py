from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_post/', add_post, name='add_post'),
    path('feedback/', feedback, name='feedback'),
    path('sign_in/', sign_in, name='sign-in'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]