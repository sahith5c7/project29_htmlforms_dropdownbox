# Generated by Django 4.2.7 on 2024-01-04 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_accessrecord_webpage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage'),
        ),
    ]