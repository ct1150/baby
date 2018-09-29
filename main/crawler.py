from main.models import *
import requests
import json


def get_category():
    category_url = 'https://tools.seeyouyima.com/taboo_category_list?v=1.0.3&app_id=11&platform=7&myclient=1171030000'
    category_response = requests.get(category_url)
    data = json.loads(category_response.content)
    # 入库
    for i in data['category_list']:
        Category.objects.create(**i)


def get_subcategory():
    id_list = Category.objects.values("id")
    subcategory_url = 'https://tools.seeyouyima.com/taboo/search?v=1.0.3&app_id=11&platform=7&myclient=1171030000'
    for category_id in id_list:
        for start in [0, 20, 40, 60, 80, 120]:
            list_param = {
                "category_id": category_id['id'],
                "size": 20,
                "start": start,
                "crowd": 0,
                "matters": 0
            }
            subcategory_list = requests.post(subcategory_url, data=list_param)
            data = json.loads(subcategory_list.content)
            for i in data:
                Subcategory.objects.create(**i)

def get_detail():
    id_list = Subcategory.objects.values("id")
    for id in id_list:
        detail_url = 'https://tools.seeyouyima.com/taboo/food?id=%d&v=1.0.3&app_id=11&platform=7&myclient=1171030000' % id['id']
        data = json.loads(requests.get(detail_url).content)
        Detail.objects.create(**data)