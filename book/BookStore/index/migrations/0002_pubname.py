# Generated by Django 3.2.19 on 2023-08-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubname', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
    ]