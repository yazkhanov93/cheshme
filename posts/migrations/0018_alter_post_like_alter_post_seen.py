# Generated by Django 4.1.6 on 2023-02-24 13:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0017_alter_userinterests_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='like sany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='seen',
            field=models.ManyToManyField(blank=True, related_name='seen', to=settings.AUTH_USER_MODEL, verbose_name='görülen sany'),
        ),
    ]
