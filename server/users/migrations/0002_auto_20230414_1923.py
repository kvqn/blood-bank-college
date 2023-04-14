# Generated by Django 4.1.5 on 2023-04-14 19:23

from django.db import migrations
from users.models import Profile

def add_users(apps, schema_editor):
    Profile.objects.create(
        username='mihir',
        password='mihir',
        email="mihir@example.com",
        first_name="Mihir",
        last_name="Kumar",
        phone="9643522963",
        blood_group="O+",
        state="Delhi",
        city="Delhi",
        pincode=110029,
        date_of_birth="2002-12-06",
        weight=110,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_users)
    ]
