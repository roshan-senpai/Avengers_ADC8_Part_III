# Generated by Django 3.0.1 on 2020-02-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='files',
            field=models.FileField(blank='True', null='True', upload_to='files/'),
            preserve_default='True',
        ),
    ]
