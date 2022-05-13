# Generated by Django 4.0.4 on 2022-05-12 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogek_app', '0002_dog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='joke',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jokes', to=settings.AUTH_USER_MODEL),
        ),
    ]