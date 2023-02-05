# Generated by Django 4.1.5 on 2023-02-05 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.car')),
            ],
        ),
    ]
