# Generated by Django 4.1.6 on 2023-04-28 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma_app', '0006_savatitm_buyurtma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='savatitm',
            name='mahsulot',
        ),
        migrations.RemoveField(
            model_name='savatitm',
            name='savat',
        ),
        migrations.DeleteModel(
            name='Buyurtma',
        ),
        migrations.DeleteModel(
            name='Savat',
        ),
        migrations.DeleteModel(
            name='SavatItm',
        ),
    ]
