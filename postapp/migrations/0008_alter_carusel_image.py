# Generated by Django 5.0.1 on 2024-02-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0007_carusel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carusel',
            name='image',
            field=models.FileField(upload_to='carusel_img'),
        ),
    ]
