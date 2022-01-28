from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Bookmark(BaseModel):
    url = models.URLField(null=True, unique=False)
    image = models.URLField(null=True, unique=False)
    title = models.TextField(unique=False)
    description = models.TextField(unique=False)
