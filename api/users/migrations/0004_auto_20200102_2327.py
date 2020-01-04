# Generated by Django 3.0.1 on 2020-01-02 23:27

from django.db import migrations
from django.contrib.auth.hashers import make_password


USERS = [
    {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "password": "secret",
    },
]

def add_initial_users(apps, schema_editor):
    User = apps.get_model("users", "User")

    for u in USERS:
        user = User.objects.create(
            username=u.get("username"),
            email=u.get("email"),
            password=make_password(u.get("password")),
            is_active=True,
            is_superuser = False,
            is_staff = True,
        )

        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200102_2102'),
    ]

    operations = [
        migrations.RunPython(add_initial_users),
    ]
