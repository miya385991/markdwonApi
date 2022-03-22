from django.db import models
from datetime import datetime
# Create your models here.

def load_path(instans,failename):
    now = datetime.now()
    return '/'.join(['image', str(now)+str('.jpg')])

class Markdown(models.Model):
    title = models.CharField(max_length=30, blank=False)
    overview = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=30, blank=False)
    author = models.CharField(max_length=30, blank=False)
    # img = models.ImageField(blank=False, null=True, upload_to=load_path)
    text = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


