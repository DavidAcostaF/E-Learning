# Generated by Django 4.1 on 2022-09-15 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0004_alter_classposts_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='UploadFiles')),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='ClassPosts',
            new_name='Posts',
        ),
        migrations.DeleteModel(
            name='UploadFiles',
        ),
        migrations.AddField(
            model_name='files',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='learning.posts'),
        ),
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
