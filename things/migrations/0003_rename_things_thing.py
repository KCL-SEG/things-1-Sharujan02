# Generated by Django 5.0 on 2023-12-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_alter_things_description_alter_things_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things',
            new_name='Thing',
        ),
    ]