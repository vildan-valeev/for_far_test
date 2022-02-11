from rest_framework.response import Response
from rest_framework import status as st


class CustomResponse(Response):
    def __init__(self, message=None, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super().__init__(
            data=data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type
        )


class OkResponse(Response):
    def __init__(self, message: str = None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        data = {'ok': message or 'Чеки успешно созданы'}
        if not status:
            status = st.HTTP_200_OK

        super().__init__(
            data=data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type
        )


class ErrorResponse(Response):
    def __init__(self, message: str = None, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        data = {'error': message or 'Ошибка ёпта!'}
        custom_status = st.HTTP_400_BAD_REQUEST
        super().__init__(
            data=data,
            status=custom_status,
            template_name=None,
            headers=None,
            exception=False,
            content_type=None
        )
