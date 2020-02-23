from django.db import models
from djmoney.models.fields import MoneyField

from api.users.models import User


class Account(models.Model):
    """User account."""
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    name = models.CharField('Name', max_length=50, blank=False)
    description = models.TextField('Description', max_length=255, default='')
    balance = MoneyField('Balance', max_digits=14, decimal_places=2, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at', 'name']
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.name
