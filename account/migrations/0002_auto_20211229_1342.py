# Generated by Django 3.0.5 on 2021-12-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(default='', max_length=250, verbose_name='about'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='level',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
