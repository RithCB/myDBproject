# Generated by Django 5.0.7 on 2024-08-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0026_kampongchnang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kohkong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gpath', models.CharField(max_length=120, verbose_name='Gpath')),
                ('Gpath1', models.CharField(max_length=120, verbose_name='Gpath1')),
                ('Gpath2', models.CharField(max_length=120, verbose_name='Gpath2')),
                ('Gpath3', models.CharField(max_length=120, verbose_name='Gpath3')),
                ('Gpath4', models.CharField(max_length=120, verbose_name='Gpath4')),
                ('Gpath5', models.CharField(max_length=120, verbose_name='Gpath5')),
                ('Gpath6', models.CharField(max_length=120, verbose_name='Gpath6')),
                ('Gpath7', models.CharField(max_length=120, verbose_name='Gpath7')),
            ],
        ),
    ]
