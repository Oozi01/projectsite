# Generated by Django 4.0.4 on 2022-05-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]