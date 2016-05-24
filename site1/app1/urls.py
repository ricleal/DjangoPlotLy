from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    # /app1
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
    url(r'^plot2d/$', views.Plot2DView.as_view(), name='plot2d'),
    url(r'^plot3d/$', views.Plot3DView.as_view(), name='plot3d'),
    url(r'^plot1d_multiple/(?P<n>\d+)/$', views.Plot1DMultipleView.as_view(), name='plot1d_multiple'),
    url(r'^plot1d_multiple_ajax/(?P<n>\d+)/$', views.plot1d_multiple_ajax, name='plot1d_multiple_ajax'),
    url(r'^plotIq/$', views.PlotIqView.as_view(), name='plotIq'),

]
