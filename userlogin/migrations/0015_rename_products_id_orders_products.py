# Generated by Django 3.2.6 on 2021-09-15 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0014_auto_20210915_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='products_id',
            new_name='products',
        ),
    ]