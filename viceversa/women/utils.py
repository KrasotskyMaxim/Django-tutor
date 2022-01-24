from .models import *
from django.db.models import Count


menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "New Post", 'url_name': "add_post"},
    {'title': "Feedback", 'url_name': "feedback"},
    ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context 