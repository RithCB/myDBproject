# Generated by Django 5.0.7 on 2024-08-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0033_rename_tamok_oudormeanchey_khaet_bos_tamok'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smallest', models.CharField(max_length=120, verbose_name='smallest')),
                ('smallest1', models.CharField(max_length=120, verbose_name='smallest1')),
                ('smallest2', models.CharField(max_length=120, verbose_name='smallest2')),
            ],
        ),
        migrations.CreateModel(
            name='Pailin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diamond', models.CharField(max_length=120, verbose_name='jav_jit')),
                ('diamond1', models.CharField(max_length=120, verbose_name='diamond1')),
                ('diamond2', models.CharField(max_length=120, verbose_name='diamond2')),
            ],
        ),
    ]
