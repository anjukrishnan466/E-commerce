# Generated by Django 3.2.6 on 2021-10-05 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0017_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='referal_code',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
