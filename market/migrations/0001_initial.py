# Generated by Django 4.1.5 on 2023-02-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('available', models.IntegerField(default=0)),
                ('image', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]
