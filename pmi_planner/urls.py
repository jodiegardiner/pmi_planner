from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.get_index, name="index"),
    url(r'^create/', core_views.create_client, name="create"),
    url(r'', include(accounts_urls)),
]
