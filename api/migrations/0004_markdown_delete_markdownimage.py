# Generated by Django 4.0.3 on 2022-03-21 03:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_markdownimage_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Markdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('overview', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('img_name', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, null=True, upload_to=api.models.load_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MarkdownImage',
        ),
    ]