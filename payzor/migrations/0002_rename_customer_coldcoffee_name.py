# Generated by Django 4.0.4 on 2022-05-27 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payzor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coldcoffee',
            old_name='customer',
            new_name='name',
        ),
    ]