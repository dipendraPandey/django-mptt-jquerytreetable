from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Genre
from .serializers import GenreSerializers


# class GenreApiView(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Genre.objects.all()
#         serializer = GenreSerializers(
#             queryset, many=True, context={'request': request})
#         response = {
#             'errors': False,
#             'message': "all genre invoked",
#             'data': serializer.data
#         }
#         return Response(response)

@api_view(['GET', ])
def genre_list_view(request):
    if request.method == 'GET':
        queryset = Genre.objects.all()
        serializer = GenreSerializers(queryset, many=True)
        response_data = {
            "error": False,
            "message": "all genre invoked",
            'data': serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "error": True,
            "message": "something went wrong",
        }
        return Response(response_data)
