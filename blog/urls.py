from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.post_list, name='post_list'), #^$ nic - tzn. homepage - když tam někdo přijde, ukáže mu to to, co vrátí fce post list
]
