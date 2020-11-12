# -*- coding: utf-8 -*-
from django.db import models


class Client(models.Model):
    """Client model. """
    du = models.IntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=100)
    total = models.FloatField()
