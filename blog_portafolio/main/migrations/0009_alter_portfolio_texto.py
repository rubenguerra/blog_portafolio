# Generated by Django 4.1 on 2022-09-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_portfolio_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='texto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
