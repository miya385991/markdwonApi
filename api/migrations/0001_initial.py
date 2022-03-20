# Generated by Django 4.0.3 on 2022-03-20 06:29

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkdownImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, null=True, upload_to=api.models.load_path)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]