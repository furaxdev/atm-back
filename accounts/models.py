# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    fingerprint_id = models.IntegerField()
    Balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name
