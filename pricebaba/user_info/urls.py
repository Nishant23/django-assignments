from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addUser/$', views.addUser, name = 'addUser'),
    url(r'^addUser/Add$', views.Add, name = 'Add'),
    url(r'^edit/q=(?P<pk>\d+)$', views.edit, name = 'edit'),
    url(r'^edit/Update$', views.Update, name = 'Update'),
]
