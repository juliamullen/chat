from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^$', views.chat_list, name='list'),
]
