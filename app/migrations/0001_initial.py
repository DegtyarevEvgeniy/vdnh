# Generated by Django 4.1.5 on 2023-02-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=2000)),
                ('time', models.CharField(max_length=200)),
                ('distance', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('placetype', models.CharField(max_length=100)),
            ],
        ),
    ]