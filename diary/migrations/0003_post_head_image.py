# Generated by Django 4.2.2 on 2023-06-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_post_updated_at_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='diary/images/%Y/%m/%d'),
        ),
    ]
