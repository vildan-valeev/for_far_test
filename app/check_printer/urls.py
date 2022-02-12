from django.urls import path, include

from check_printer.views import CreateChecks, NewChecks

urlpatterns = [
    path('create_checks/', CreateChecks.as_view()),
    path('new_checks/<str:api_key>/', NewChecks.as_view()),
    # path('check/', CheckGetPDF.as_view()),
    path('django-rq/', include('django_rq.urls'))
]
