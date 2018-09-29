from django.shortcuts import render
from django.http import HttpResponse
from main.crawler import *
from main.serializers import CategorySerializer,SubCategorySerializer,DetailSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
def crawler(requests):
    get_category()
    return HttpResponse("category抓取完成")


def subcategory(requests):
    get_subcategory()
    return HttpResponse("subcategory抓取完成")


def detail(requests):
    get_detail()
    return HttpResponse("detail抓取完成")


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)


class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category_id',)

class DetailViewset(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)