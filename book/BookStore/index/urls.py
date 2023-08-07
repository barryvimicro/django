from django.urls import path
from index import views
app_name='index'

urlpatterns=[
    path('test/',views.index_html,name='detail_hello'),  #127.0.0.1:800/index/test  访问子模板
    path('base/',views.base_html),   #127.0.0.1:8000/index/base 返回问父模板
    path('redict/',views.redict_url),
    path('reverse/',views.test_to_reverse),
    path("allbook/",views.BookName),

]