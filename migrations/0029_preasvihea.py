# Generated by Django 5.0.7 on 2024-08-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0028_kratie'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreasVihea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkthailand', models.CharField(max_length=120, verbose_name='fkthailand')),
                ('fkthailand1', models.CharField(max_length=120, verbose_name='fkthailand1')),
                ('fkthailand2', models.CharField(max_length=120, verbose_name='fkthailand2')),
                ('fkthailand3', models.CharField(max_length=120, verbose_name='fkthailand3')),
                ('fkthailand4', models.CharField(max_length=120, verbose_name='fkthailand4')),
                ('fkthailand5', models.CharField(max_length=120, verbose_name='fkthailand5')),
                ('fkthailand6', models.CharField(max_length=120, verbose_name='fkthailand6')),
                ('fkthailand7', models.CharField(max_length=120, verbose_name='fkthailand7')),
                ('fkthailand8', models.CharField(max_length=120, verbose_name='fkthailand8')),
            ],
        ),
    ]
