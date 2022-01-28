from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"


class CreateBookmarkSerliazer(serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = Bookmark
        fields = ["url"]
