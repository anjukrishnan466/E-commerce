# Generated by Django 3.2.6 on 2021-09-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart1',
            name='user_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]