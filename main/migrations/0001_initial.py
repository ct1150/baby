# Generated by Django 2.1.1 on 2018-09-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldid', models.IntegerField()),
                ('icon', models.URLField()),
                ('sort', models.IntegerField()),
                ('title', models.CharField(max_length=10)),
            ],
        ),
    ]
