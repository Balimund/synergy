from django.db import models


class UserName(models.Model):
    """Имя пользователя, введённое в форме."""

    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name
