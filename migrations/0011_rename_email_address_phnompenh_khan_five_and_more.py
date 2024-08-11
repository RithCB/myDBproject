# Generated by Django 5.0.7 on 2024-08-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0010_rename_venue_phnompenh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phnompenh',
            old_name='email_address',
            new_name='khan_five',
        ),
        migrations.RenameField(
            model_name='phnompenh',
            old_name='address',
            new_name='khan_four',
        ),
        migrations.RenameField(
            model_name='phnompenh',
            old_name='name',
            new_name='khan_one',
        ),
        migrations.RenameField(
            model_name='phnompenh',
            old_name='web',
            new_name='khan_six',
        ),
        migrations.RenameField(
            model_name='phnompenh',
            old_name='zip_code',
            new_name='khan_three',
        ),
        migrations.RenameField(
            model_name='phnompenh',
            old_name='phone',
            new_name='khan_two',
        ),
        migrations.AddField(
            model_name='kandal',
            name='twelve_dis',
            field=models.CharField(default='twelve_dis', max_length=120),
        ),
        migrations.AddField(
            model_name='phnompenh',
            name='khan_fifteen',
            field=models.CharField(default='khanti15', max_length=120),
        ),
    ]
