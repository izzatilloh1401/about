# Generated by Django 5.0.1 on 2024-01-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_comments_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={},
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.FileField(default='comment_images/user.png', upload_to='comment-images'),
        ),
    ]