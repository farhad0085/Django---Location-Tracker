# Generated by Django 3.1.2 on 2020-10-13 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='uploaded_by',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='location.device'),
        ),
    ]
