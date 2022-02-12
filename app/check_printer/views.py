from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from check_printer.custom_responses import OkResponse, ErrorResponse
from check_printer.serializers import OrderSerializer, CheckSerializer
from check_printer.services import create_checks


class CreateChecks(APIView):
    """Вьюха на создание чеков"""
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            result, message = create_checks(serializer.validated_data)
            if result:
                return OkResponse(message, status=210)
            else:
                return ErrorResponse(message, status=400)
        return Response(serializer.errors, status=400)


class NewChecks(ListAPIView):
    serializer_class = CheckSerializer
    model = serializer_class.Meta.model

    def get_queryset(self, ):
        z = self.model.objects.filter(printer_id__api_key=self.kwargs['api_key'])
        print(z)
        return self.model.objects.filter(printer_id__api_key=self.kwargs['api_key'])
    # def get(self, request, api_key, *args, **kwargs):
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print('CREATING', serializer.validated_data)
    #         return OkResponse('заебись', status=210)
    #         # return ErrorResponse('gbpltw', status=400)
    #     return Response(serializer.errors, status=400)

# class NewChecks(APIView):
#     pass


# class CheckGetPDF(RetrieveAPIView):
#     pass
