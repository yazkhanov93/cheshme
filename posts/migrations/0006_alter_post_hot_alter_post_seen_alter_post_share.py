# Generated by Django 4.1.6 on 2023-02-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hot',
            field=models.PositiveIntegerField(blank=True, default='0', null=True, verbose_name='gyzgynlygy'),
        ),
        migrations.AlterField(
            model_name='post',
            name='seen',
            field=models.PositiveIntegerField(blank=True, default='0', null=True, verbose_name='görülen sany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='share',
            field=models.PositiveIntegerField(blank=True, default='0', null=True, verbose_name='paýlaşylan sany'),
        ),
    ]
