# Generated by Django 5.1.2 on 2024-11-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="txid",
            field=models.TextField(unique=True),
        ),
    ]
