# Generated by Django 2.1.1 on 2018-09-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180913_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='title_alias',
            field=models.CharField(max_length=100),
        ),
    ]