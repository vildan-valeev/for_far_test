from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from check_printer.custom_responses import OkResponse
from check_printer.serializers import OrderSerializer, CheckSerializer


class CreateChecks(APIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            print('CREATING', serializer.validated_data)
            return OkResponse('заебись', status=210)
            # return ErrorResponse('gbpltw', status=400)
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
