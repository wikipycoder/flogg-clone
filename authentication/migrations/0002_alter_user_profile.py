# Generated by Django 4.0 on 2022-01-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
