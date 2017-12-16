from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=30)
    realname = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    description = models.TextField(default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Photograph (models.Model):
    owner = models.ForeignKey(User)
    created = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images/', default='')
    description = models.TextField(null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.owner.name + ' ' + str(self.created)


class Comment(models.Model):
    author = models.CharField(max_length=30)
    photograph = models.ForeignKey(Photograph)
    text = models.TextField(default='')

    def __str__(self):
        return 'Author: ' + self.author + ' Photo: ' + str(self.photograph)




