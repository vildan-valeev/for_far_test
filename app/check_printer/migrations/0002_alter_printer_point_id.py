# Generated by Django 4.0.2 on 2022-02-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_printer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='point_id',
            field=models.IntegerField(help_text='точка к которой привязан принтер', verbose_name='ID точки'),
        ),
    ]