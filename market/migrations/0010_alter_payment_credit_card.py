# Generated by Django 4.1.5 on 2023-02-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_alter_payment_amount_alter_payment_credit_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='credit_card',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]