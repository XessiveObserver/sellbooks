from distutils.command.upload import upload
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%d/%m/%Y/', blank=True, null=True)
    cover_photo = models.ImageField(
        upload_to='users/%d/%m/%Y/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    @property
    def cover_url(self):
        if self.cover_photo and hasattr(self.cover_photo, 'url'):
            return self.cover_photo.url
