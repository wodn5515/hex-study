# Generated by Django 5.1.4 on 2024-12-31 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_author_alter_postentity_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='AuthorEntity',
        ),
    ]