# Generated by Django 4.1.4 on 2023-03-16 09:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0027_rename_periodic_action_period_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='action',
            unique_together={('person', 'title', 'date')},
        ),
    ]