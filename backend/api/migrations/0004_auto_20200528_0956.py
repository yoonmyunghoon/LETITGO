# Generated by Django 3.0.6 on 2020-05-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200528_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]
