# Generated by Django 2.1.1 on 2018-09-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180913_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldid', models.IntegerField()),
                ('baby_comment', models.CharField(max_length=30)),
                ('baby_notice', models.IntegerField()),
                ('baby_notice_month', models.IntegerField()),
                ('category', models.IntegerField()),
                ('cookbook', models.BooleanField(blank=True, null=True)),
                ('copywriting', models.CharField(max_length=20)),
                ('icon', models.URLField()),
                ('img', models.URLField()),
                ('lactation_comment', models.CharField(max_length=100)),
                ('lactation_notice', models.IntegerField()),
                ('nutrition', models.TextField()),
                ('pregnant_comment', models.TextField()),
                ('pregnant_notice', models.IntegerField()),
                ('puerpera_comment', models.TextField()),
                ('puerpera_notice', models.IntegerField()),
                ('recommend_url', models.URLField(blank=True, null=True)),
                ('restriction', models.BooleanField(blank=True, null=True)),
                ('sort', models.IntegerField()),
                ('strategy', models.TextField()),
                ('taboo_ingredient', models.TextField()),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldid', models.IntegerField()),
                ('baby_notice', models.IntegerField()),
                ('baby_notice_month', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('icon', models.URLField()),
                ('loctation', models.IntegerField()),
                ('nutrition', models.CharField(max_length=100)),
                ('pregnant_notice', models.IntegerField()),
                ('puerpera_notice', models.IntegerField()),
                ('restriction', models.BooleanField(blank=True, null=True)),
                ('sort', models.IntegerField()),
                ('title', models.CharField(max_length=10)),
                ('title_alias', models.CharField(max_length=20)),
            ],
        ),
    ]
