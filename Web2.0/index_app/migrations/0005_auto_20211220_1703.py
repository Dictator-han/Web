# Generated by Django 3.2.5 on 2021-12-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_app', '0004_auto_20211220_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhixiao',
            name='shangfen',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zhixiao',
            name='shenfen',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zhixiao',
            name='sufen',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zhixiao',
            name='tianfen',
            field=models.CharField(max_length=32),
        ),
    ]