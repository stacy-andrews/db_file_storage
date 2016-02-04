# django
from django.conf.urls import patterns, url
from db_file_storage.views import get_file

urlpatterns = [
    url(
        r'^download/',
        get_file,
        {'add_attachment_headers': True},
        name='db_file_storage.download_file'
    ),
    url(
        r'^get/',
        get_file,
        {'add_attachment_headers': False},
        name='db_file_storage.get_file'
    )
]
