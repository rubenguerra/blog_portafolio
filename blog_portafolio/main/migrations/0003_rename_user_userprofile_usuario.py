# Generated by Django 4.1 on 2022-08-09 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_usuario_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='usuario',
        ),
    ]