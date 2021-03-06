from django.db import models
from djmoney.models.fields import MoneyField

from api.users.models import User


class Account(models.Model):
    """User account"""
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    name = models.CharField('Name', max_length=50, blank=False)
    description = models.TextField('Description', max_length=255, default='')
    balance = MoneyField(
        'Balance',
        max_digits=14,
        decimal_places=2,
        blank=False,
        null=False,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at', 'name']
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Transaction category"""
    DEFAULT = 'def'
    CUSTOM = 'cus'
    TYPES = [
        (DEFAULT, 'Default'),
        (CUSTOM, 'Custom'),
    ]

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    name = models.CharField('Name', max_length=50, blank=False)
    description = models.TextField('Description', max_length=255, default='')
    type = models.CharField(
        'Type',
        choices=TYPES,
        default=CUSTOM,
        max_length=3,
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name} ({self.get_type_display()})'


class Transaction(models.Model):
    """Transaction"""
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    name = models.CharField('Name', max_length=50, blank=False)
    description = models.TextField('Description', max_length=255, default='')
    value = models.DecimalField(
        'Value',
        max_digits=14,
        decimal_places=2,
        blank=False,
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
