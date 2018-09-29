from main.models import *
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("icon", "id", "sort", "title",)


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subcategory
        fields = ("baby_notice", "baby_notice_month", "category_id", "icon", "id", "lactation_notice", "nutrition",
                  "pregnant_notice", "puerpera_notice", "restriction", "sort", "title", "title_alias")


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detail
        # fields = "__all__"
        fields = (
            "baby_comment", "baby_notice", "baby_notice_month", "category", "cookbook", "copywriting", "icon", "id",
            "img", "lactation_comment", "lactation_notice", "nutrition", "pregnant_comment", "pregnant_notice",
            "puerpera_comment", "puerpera_notice", "recommend_url", "restriction", "sort", "strategy",
            "taboo_ingredient", "title",)
