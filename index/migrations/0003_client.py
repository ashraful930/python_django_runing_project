# Generated by Django 3.2.7 on 2021-11-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=700)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]
