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
    url(r'^update_add/', core_views.update_address, name="update_add"),
    url(r'^update_email/', core_views.update_email, name="update_email"),
    url(r'^update_phone/', core_views.update_phone, name="update_phone"),
    url(r'^update_c_notes/', core_views.update_c_notes, name="update_c_notes"),
    url(r'^update_p_notes/', core_views.update_p_notes, name="update_p_notes"),
    url(r'^update_due_date/', core_views.update_due_date, name="update_due_date"),

    url(r'', include(accounts_urls)),
    url(r'', include(forum_urls)),
]
