# Generated by Django 4.0 on 2022-01-14 18:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0002_alter_member_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='student',
            field=models.ManyToManyField(related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
