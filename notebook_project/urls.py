from django.contrib import admin
from django.urls import include, path

from notes import urls as notes_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(notes_urls)),
]
