# Generated by Django 3.0.5 on 2021-12-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211229_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(max_length=20),
        ),
    ]
