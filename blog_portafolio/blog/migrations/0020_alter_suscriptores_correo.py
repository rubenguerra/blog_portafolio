# Generated by Django 4.1 on 2023-03-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_suscriptores_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscriptores',
            name='correo',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]