# Generated by Django 4.1.3 on 2022-11-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
