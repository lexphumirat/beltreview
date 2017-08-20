# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

# class UserManager(models.Manager):
#     User.objects.create(
#     full_name = request.POST['full_name'],
#     alias = request.POST['alias']
#     )


class User(models.Model):
    full_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.full_name + " " + self.email
