# baby
## 抓取母婴食谱并生成api接口，使用django+rest_framework框架
```
#三个uri分别抓取食物种类、子类列表、食物详情并入mysql库
    #path('crawler/', crawler),
    #path('sub/', subcategory),
    #path('detail/', detail),
    
#直接请求根路径返回api
path('',include(router.urls)),

```
