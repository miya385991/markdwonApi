from django.db import models
# Create your models here.

def load_path(instance, filename):
    return '/'.join(['image', str(instance.title)+str('.jpg')])

class MarkdownImage(models.Model):
    title = models.CharField(max_length=30, blank=False)
    img = models.ImageField(blank=True, null=True, upload_to=load_path)
    created = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return self.title