from collections import OrderedDict

from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from check_printer.custom_render import BinaryFileRenderer
from check_printer.custom_responses import OkResponse, ErrorResponse
from check_printer.models import Check
from check_printer.serializers import OrderSerializer, CheckSerializer
from check_printer.service.create_check import create_checks
from check_printer.service.get_pdf_file import get_pdf_check_file


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
        if not queryset:
            return ErrorResponse('Ошибка авторизации', status=401)
        page = self.paginate_queryset(queryset) or queryset
        serializer = self.get_serializer(page, many=True)
        return Response({'checks': serializer.data, })

    def get_queryset(self, ):
        return self.model.objects.filter(printer_id__api_key=self.kwargs['api_key'])


class CheckGetPDF(APIView):
    renderer_classes = (BinaryFileRenderer,)

    def get(self, request, *args, **kwargs):
        # print(self.kwargs.get('api_key'), self.kwargs.get('check_id'))
        file, message, code = get_pdf_check_file(**kwargs)
        # print(file)
        if file:
            # return OkResponse('message', status=210)
            print(file.name, file.path)
            with open(file.path, 'rb') as report:
                return Response(
                    report.read(),
                    headers={'Content-Disposition': f'attachment; filename="{file.name}"'},
                    content_type='application/pdf')
        else:
            return ErrorResponse(message, status=code)