# Generated by Django 3.2.5 on 2021-12-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_app', '0003_auto_20211220_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='zhixiao',
            name='one',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zhixiao',
            name='two',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
