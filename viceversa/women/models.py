from os import urandom
from statistics import mode
from django.db import models
from django.urls import reverse


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Description")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated")
    is_published = models.BooleanField(default=True, verbose_name="Published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Celebrity womens"
        verbose_name_plural = "Celebrity womens"
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
        ordering = ['id']