# Generated by Django 4.1.6 on 2023-03-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_optioninfo_downfactor_alter_optioninfo_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optioninfo',
            name='downfactor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='optioninfo',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='optioninfo',
            name='timeperiod',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='optioninfo',
            name='upfactor',
            field=models.IntegerField(),
        ),
    ]
