from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=70) # len('llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogochuchaf.org.uk')
    visiting_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name