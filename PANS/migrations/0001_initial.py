# Generated by Django 3.0.5 on 2021-12-29 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pancategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='payofpansdue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankaccount', models.CharField(max_length=50)),
                ('bankname', models.CharField(max_length=50)),
                ('bank', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year1', models.CharField(blank=True, max_length=50, null=True)),
                ('year2', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.FileField(upload_to='')),
                ('active', models.BooleanField(blank=True, null=True)),
                ('activity', models.CharField(max_length=225)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sected', to='PANS.pancategory')),
            ],
        ),
    ]
