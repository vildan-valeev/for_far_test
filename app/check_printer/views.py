from collections import OrderedDict

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from check_printer.custom_responses import OkResponse, ErrorResponse
from check_printer.serializers import OrderSerializer, CheckSerializer
from check_printer.service.create_check import create_checks


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

    def list(self, request, *args, **kwargs):
        """переопределяем list, убираем metadata"""
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset) or queryset
        serializer = self.get_serializer(page, many=True)
        return Response({'checks': serializer.data, })

    def get_queryset(self, ):
        z = self.model.objects.filter(printer_id__api_key=self.kwargs['api_key'])
        print(z)
        return self.model.objects.filter(printer_id__api_key=self.kwargs['api_key'])


# class CheckGetPDF(RetrieveAPIView):
#     pass
