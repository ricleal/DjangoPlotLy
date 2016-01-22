from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    # /app1
    url(r'^$', views.IndexView.as_view(), name='index'),
]
