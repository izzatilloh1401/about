# Generated by Django 5.0.1 on 2024-01-30 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_comments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='postapp.comments'),
        ),
    ]
