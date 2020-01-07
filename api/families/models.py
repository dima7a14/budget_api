from django.db import models

from api.users.models import User


class Family(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    name = models.CharField('Name', max_length=30, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # TODO: set owner as another user in the family.
    members = models.ManyToManyField(User, related_name="members")

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'families'

    def __str__(self):
        return self.name

