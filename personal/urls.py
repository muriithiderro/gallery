from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^search/', views.home, name='search'),
    # url(r'^search', views.SearchListView.as_view(), name='search'),


]