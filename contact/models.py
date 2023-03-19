from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=30)
    contact_image = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name_plural = _('Contact List')
