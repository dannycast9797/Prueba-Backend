# Generated by Django 3.2.8 on 2021-10-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]