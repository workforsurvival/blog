from django.db import models
from django.urls import reverse
from django.shortcuts import resolve_url


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    companyName = models.CharField(max_length=100)
    companyPerson = models.CharField(max_length=100)
    companyTel = models.CharField(max_length=100)
    companyEmail = models.EmailField()
    companyComment = models.TextField()
    isView = models.BooleanField(default=False)

    def __str__(self):
        return self.companyName + " " + self.companyPerson

    def get_absolute_url(self):
        return resolve_url("../home/")
