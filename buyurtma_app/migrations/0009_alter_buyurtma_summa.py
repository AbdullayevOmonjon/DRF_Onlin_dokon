# Generated by Django 4.1.6 on 2023-04-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma_app', '0008_savat_savatitm_buyurtma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyurtma',
            name='summa',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
