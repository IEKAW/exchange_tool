from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.input_form),
    url(r'^export.csv$', views.export_csv),
]
