# Generated by Django 4.1 on 2022-09-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0014_remove_files_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='qualification',
            new_name='grade',
        ),
    ]
