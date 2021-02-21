""" users models."""
# django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model.

    proxym model that extends the base data with order information

    Args:
        models (models.Model): django model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=250, blank=True)
    biography = models.TextField(blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/images',
        blank=True,
            null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modifed = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """__str__

        Returns:
            str: username
        """
        return self.user.username
