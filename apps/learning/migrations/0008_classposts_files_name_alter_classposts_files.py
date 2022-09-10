# Generated by Django 4.1 on 2022-09-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_classposts_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='classposts',
            name='files_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='classposts',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files_posts'),
        ),
    ]
