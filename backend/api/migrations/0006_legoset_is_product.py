# Generated by Django 3.0.6 on 2020-06-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200613_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='legoset',
            name='is_product',
            field=models.IntegerField(default=1),
        ),
    ]