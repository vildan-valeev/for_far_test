from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from check_printer.custom_responses import OkResponse, ErrorResponse
from check_printer.serializers import OrderSerializer


class CreateChecks(APIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            print('CREATING', serializer.validated_data)
            return OkResponse('заебись', status=210)
            # return ErrorResponse('gbpltw', status=400)
        return Response(serializer.errors, status=400)


# class NewChecks(APIView):
#     pass


# class CheckGetPDF(RetrieveAPIView):
#     pass
