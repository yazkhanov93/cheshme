# Generated by Django 4.1.6 on 2023-02-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_like_alter_post_seen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserId',
        ),
    ]
