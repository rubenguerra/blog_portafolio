# Generated by Django 4.1 on 2022-08-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_user_userprofile_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='es_activo',
            field=models.BooleanField(default=True),
        ),
    ]