# Generated by Django 3.0.1 on 2020-02-10 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, verbose_name='Team Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('contact', models.IntegerField(verbose_name='Contact ')),
            ],
        ),
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
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100, verbose_name='Field Name')),
                ('field_address', models.CharField(max_length=100, verbose_name='Field Address')),
                ('field_contact', models.IntegerField(verbose_name='Field Contact')),
                ('customer_field', models.ManyToManyField(to='restapi.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('charge', models.IntegerField(verbose_name='charge')),
                ('bill', models.CharField(max_length=100, verbose_name='Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(verbose_name='Contact')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('staff_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Field')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_payment',
            field=models.ManyToManyField(to='restapi.Payment'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('charge', models.IntegerField(verbose_name='charge')),
                ('payment', models.IntegerField(verbose_name='Payment')),
                ('team_name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('customer_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Customer')),
            ],
        ),
    ]
