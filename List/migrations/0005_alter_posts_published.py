# Generated by Django 5.0.6 on 2024-07-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0004_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published',
            field=models.BooleanField(),
        ),
    ]