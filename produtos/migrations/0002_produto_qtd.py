# Generated by Django 3.1.3 on 2021-07-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='qtd',
            field=models.PositiveIntegerField(default=0),
        ),
    ]