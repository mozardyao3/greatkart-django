# Generated by Django 3.2.3 on 2021-05-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress_line_1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress_line_2',
            new_name='address_line_2',
        ),
    ]
