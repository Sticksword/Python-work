from django.db import models
from django.db.models import permalink
import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Bulletin(models.Model):
    blog_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, unique=True)
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=100, unique=True)
    body = models.CharField(max_length=100, unique=True)