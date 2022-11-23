# Generated by Django 3.2.13 on 2022-11-23 10:24

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='default_image.jpg', upload_to='profile_image/%Y/%m'),
        ),
    ]
