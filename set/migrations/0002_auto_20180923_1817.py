# Generated by Django 2.0.1 on 2018-09-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='setname',
            field=models.CharField(max_length=64, verbose_name='设置名称'),
        ),
        migrations.AlterField(
            model_name='set',
            name='setvalue',
            field=models.CharField(max_length=200, verbose_name='设置的值'),
        ),
    ]
