# Generated by Django 3.2.13 on 2023-05-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('nome', models.CharField(max_length=100)),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Passos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]