# Generated by Django 2.1.1 on 2018-11-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userReg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]