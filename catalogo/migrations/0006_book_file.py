# Generated by Django 3.0.6 on 2020-05-06 07:25

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_auto_20200506_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='files'),
        ),
    ]
