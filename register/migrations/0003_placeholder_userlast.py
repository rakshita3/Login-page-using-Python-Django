# Generated by Django 3.2.5 on 2021-07-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_placeholder_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeholder',
            name='userlast',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
