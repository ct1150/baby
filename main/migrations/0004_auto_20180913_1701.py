# Generated by Django 2.1.1 on 2018-09-13 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_detail_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='oldid',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='oldid',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='oldid',
        ),
    ]
