# Generated by Django 3.1.3 on 2021-07-24 18:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20210709_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='nome', unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='nome', unique=True),
        ),
    ]
