from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from accounts import urls as accounts_urls
from threads import urls as forum_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.get_index, name="index"),

    url(r'^client/$', core_views.client_list, name='clients'),
    url(r'^client/(?P<id>\d+)$', core_views.client_details, name='client_detail'),
    url(r'^create/', core_views.create_client, name="create"),

    url(r'', include(accounts_urls)),
    url(r'', include(forum_urls)),
]
