# Generated by Django 2.1.7 on 2019-05-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190522_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_list',
            name='cast',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Cast_List'),
        ),
    ]
