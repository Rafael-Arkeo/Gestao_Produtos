# Generated by Django 3.1.3 on 2021-07-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_auto_20210707_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
