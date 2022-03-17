from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.serializers import CreateUrlSerializer, ReturnUrlSerializer


class CreateAPI(CreateAPIView):
    serializer_class = CreateUrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateUrlSerializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.get_or_create()
            serializer = ReturnUrlSerializer(instance)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
