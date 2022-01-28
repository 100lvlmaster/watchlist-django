from django.urls import path
from bookmark.api import BookmarkApi


urlpatterns = [
    path("", BookmarkApi.as_view()),
]
