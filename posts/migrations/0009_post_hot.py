# Generated by Django 4.1.6 on 2023-02-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_taglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hot',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='gyzgynlygy'),
        ),
    ]