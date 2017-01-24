from django.conf.urls import url,include
# from django.contrib import admin
from . import views



urlpatterns = [
    url(r'top_ten/',views.top_news, name = "top_ten_news"),
    url(r'new_discr/',views.new_discr, name = "news_disc"),
]