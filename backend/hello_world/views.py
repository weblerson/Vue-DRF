from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


class HelloWorldApiView(views.APIView):

    def get(self, request):
        return Response({
            'body': 'Hello, World!'
        }, status=status.HTTP_200_OK)
