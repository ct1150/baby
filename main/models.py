from django.db import models


# Create your models here.
class Category(models.Model):
    # oldid = models.IntegerField(null=True,blank=True)
    icon = models.URLField()
    sort = models.IntegerField()
    title = models.CharField(max_length=10)


class Subcategory(models.Model):
    # oldid = models.IntegerField()
    baby_notice = models.IntegerField()
    baby_notice_month = models.IntegerField()
    category_id = models.IntegerField()
    icon = models.URLField()
    lactation_notice = models.IntegerField()
    nutrition = models.CharField(max_length=100)
    pregnant_notice = models.IntegerField()
    puerpera_notice = models.IntegerField()
    restriction = models.NullBooleanField(null=True,blank=True)
    sort = models.IntegerField()
    title = models.CharField(max_length=10)
    title_alias = models.CharField(max_length=100)


class Detail(models.Model):
    # oldid = models.IntegerField()
    baby_comment = models.TextField()
    baby_notice = models.IntegerField()
    baby_notice_month = models.IntegerField()
    category = models.IntegerField()
    cookbook = models.TextField(null=True, blank=True)
    copywriting = models.CharField(max_length=20)
    icon = models.URLField()
    img = models.URLField()
    lactation_comment = models.TextField()
    lactation_notice = models.IntegerField()
    nutrition = models.TextField()
    pregnant_comment = models.TextField()
    pregnant_notice = models.IntegerField()
    puerpera_comment = models.TextField()
    puerpera_notice = models.IntegerField()
    recommend_url = models.URLField(null=True, blank=True)
    restriction = models.NullBooleanField(null=True,blank=True)
    sort = models.IntegerField()
    strategy = models.TextField()
    taboo_ingredient = models.TextField()
    title = models.CharField(max_length=10)
