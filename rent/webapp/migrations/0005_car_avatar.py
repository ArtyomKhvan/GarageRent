# Generated by Django 3.2.8 on 2021-10-29 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_photo_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='webapp.photo', verbose_name='Аватар'),
        ),
    ]
