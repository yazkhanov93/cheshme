# Generated by Django 4.1.6 on 2023-03-08 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinterests',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='category'),
        ),
    ]