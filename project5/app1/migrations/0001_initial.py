# Generated by Django 4.0.4 on 2022-05-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('descripton', models.CharField(max_length=1000)),
            ],
        ),
    ]
