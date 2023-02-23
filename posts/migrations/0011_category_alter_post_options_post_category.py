# Generated by Django 4.1.6 on 2023-02-18 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_post_hot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ady')),
            ],
            options={
                'verbose_name_plural': 'Kategoriýalar',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Makalalar'},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='posts.category', verbose_name='kategoriýa'),
        ),
    ]