from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
    path('sign_in/', LoginUser.as_view(), name='sign-in'),
    path('sign_out/', logout_user, name='sign-out'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]