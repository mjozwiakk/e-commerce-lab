# Generated by Django 3.0.5 on 2020-05-01 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_orderproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]
