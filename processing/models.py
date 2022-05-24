from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class BookJournalBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)

class Journal(BookJournalBase):
    type_choices = ((1, "Bullet"), (2, "Food"), (3, "Travel"), (4, "Sport"))
    publisher = models.CharField(max_length=255)

