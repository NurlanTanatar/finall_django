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


# class CustomUser(AbstractUser):
#     id = models.AutoField(primary_key=True)
#     user_type_choices = ((1, "SuperAdmin"), (2, "Guest"),)
#     user_type = models.CharField(
#         max_length=255, choices=user_type_choices, default=2)

# class SuperAdminUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     profile_pic = models.FileField(default="")
#     auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class GuestUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     profile_pic = models.FileField(default="")
#     created_at = models.DateTimeField(auto_now_add=True)


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == 1:
#             SuperAdminUser.objects.create(auth_user_id=instance)
#         if instance.user_type == 2:
#             GuestUser.objects.create(auth_user_id=instance)


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.superadminuser.save()
#     if instance.user_type == 2:
#         instance.guestuser.save()