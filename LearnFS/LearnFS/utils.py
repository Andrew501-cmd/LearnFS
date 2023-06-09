import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from urllib.parse import urljoin
from datetime import datetime


class CkeditorCustomStorage(FileSystemStorage):
    def get_folder_name(self):
        return datetime.now().strftime('%Y/%m/%d')

    def get_valid_name(self, name):
        return name

    def _save(self, name, content):
        folder_name = self.get_folder_name()
        name = os.path.join(folder_name, self.get_valid_name(name))
        return super()._save(name, content)

    location = os.path.join(settings.MEDIA_ROOT, 'media/Article/img/')
    base_url = urljoin(settings.MEDIA_URL, 'media/Article/img/')