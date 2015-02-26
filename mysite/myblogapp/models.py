from django.db import models


class Post(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField('date published')


# class Post(models.Model):
#     body = models.TextField()
#     pub_date = models.DateTimeField('date published')
#     title = models.CharField(max_length=500)
#     tags = models.CharField(max_length=200)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.body


