# Generated by Django 4.0.4 on 2022-06-10 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0003_commnet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnet',
            new_name='Comment',
        ),
    ]
