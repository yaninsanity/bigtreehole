# Generated by Django 2.1.1 on 2018-11-07 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.IntegerField(primary_key=True, serialize=False)),
                ('commentword', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('contentword', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=50)),
                ('upassword', models.CharField(max_length=16)),
                ('regTime', models.DateField(auto_now=True, verbose_name='regDate')),
                ('email', models.EmailField(max_length=50)),
                ('img', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userReg.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userReg.Content'),
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userReg.User'),
        ),
    ]