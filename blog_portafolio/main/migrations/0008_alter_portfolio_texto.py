# Generated by Django 4.1 on 2022-09-11 18:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_portfolio_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
