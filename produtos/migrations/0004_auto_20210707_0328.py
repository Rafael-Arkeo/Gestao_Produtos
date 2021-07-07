# Generated by Django 3.1.3 on 2021-07-07 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='atualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
