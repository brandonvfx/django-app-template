from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='{{ app_name}}/index.html'), name='{{ app_name}}:index'),
)

