# Generated by Django 4.1 on 2022-09-05 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_rename_uuid_classroom_classroom_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classroom',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='classroom',
            name='visibility',
            field=models.IntegerField(choices=[(0, 'Visible'), (1, 'Ocult')], default=0),
        ),
    ]
