# Generated by Django 4.1.1 on 2022-10-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
