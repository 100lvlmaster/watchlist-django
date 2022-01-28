from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.response import Response
from .opengraph import get_opengraph
from bookmark.serializer import BookmarkSerializer, CreateBookmarkSerliazer


class BookmarkApi(APIView):
    serializer_class = BookmarkSerializer
    #
    def get(self, request, format=None):
        validation = CreateBookmarkSerliazer(data=request.data)
        if not validation.is_valid():
            return Response(status=HTTPStatus.BAD_REQUEST, data=validation.errors)
        og = get_opengraph(validation.data["url"])
        bookmark = BookmarkSerializer(data=og)
        if not bookmark.is_valid():
            return Response(status=HTTPStatus.BAD_REQUEST, data=bookmark.errors)
        saved = bookmark.save()
        return Response(data=saved)

    def post(self, request, format=None):

        return Response(data={"data": "data"}, status=HTTPStatus.OK)
