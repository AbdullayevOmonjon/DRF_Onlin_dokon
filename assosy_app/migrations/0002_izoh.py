# Generated by Django 4.2 on 2023-04-17 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('assosy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=300)),
                ('reyting', models.PositiveSmallIntegerField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assosy_app.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.profil')),
            ],
        ),
    ]
