# Generated by Django 3.1.5 on 2021-01-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210111_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='girl.jpeg', upload_to=None),
        ),
    ]
