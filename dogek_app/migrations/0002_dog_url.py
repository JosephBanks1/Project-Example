# Generated by Django 4.0.4 on 2022-05-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogek_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='url',
            field=models.TextField(default=''),
        ),
    ]