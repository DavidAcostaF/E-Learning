# Generated by Django 4.1 on 2022-09-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_remove_posts_files_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='upload_date',
            field=models.DateField(),
        ),
    ]