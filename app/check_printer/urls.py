from django.urls import path

from check_printer.views import CreateChecks

urlpatterns = [

    path('create_checks/', CreateChecks.as_view()),
    # path('new_checks/', NewChecks.as_view()),
    # path('check/', CheckGetPDF.as_view()),
]
