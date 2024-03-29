# Generated by Django 3.0.5 on 2021-12-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0002_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the sender', max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]
