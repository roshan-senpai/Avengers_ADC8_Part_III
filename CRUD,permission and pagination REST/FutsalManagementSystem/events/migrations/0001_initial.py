# Generated by Django 3.0.1 on 2020-01-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('venue', models.CharField(max_length=100, verbose_name='Venue')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('manager', models.CharField(max_length=100, verbose_name='Manager Name')),
            ],
        ),
    ]
