# Generated by Django 2.2.28 on 2024-02-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
