from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from core.utils import save_image_save_path
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=256)
    country = models.CharField(verbose_name=_("Country"), max_length=256)
    tel_number = models.CharField(verbose_name=_("Phone Number"), max_length=256)
    identifier_token = models.CharField(verbose_name=_("identifier token"), max_length=256)
    created_on = models.DateField(_("Created on"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated on"), auto_now=True)
    
    logo = models.ImageField(
        verbose_name=_("Image"),
        upload_to=save_image_save_path,
        blank=True,
        null=True,
        default="assets/imgs/resources/profiledefault.png",
    )

    def __str__(self):
        return self.name

class User(AbstractUser):
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to=save_image_save_path,
        blank=True,
        null=True,
        default="assets/imgs/resources/profiledefault.png",
    )
    # to be used from account activation
    is_email_activated = models.BooleanField(_("Email Activated"), default=False)

    def save(self, *args, **kwargs):
        if self.is_email_activated:
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        if self.get_username:
            return f"{self.get_username()}"
        return f"{self.first_name} {self.last_name}"
