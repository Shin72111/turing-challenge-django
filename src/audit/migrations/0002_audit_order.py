# Generated by Django 2.2.5 on 2019-09-16 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Orders'),
        ),
    ]
