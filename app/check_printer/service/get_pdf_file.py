from typing import Tuple, Union

from django.db.models.fields.files import FieldFile

from check_printer.models import Check


def get_pdf_check_file(**kwargs) -> Tuple[Union[FieldFile, None], str, int]:
    qs = Check.objects.filter(printer_id__api_key=kwargs.get('api_key'))
    if qs.exists():  # если есть чеки
        # for PostgreSQL
        # if qs.filter(order__contains={"id": kwargs.get('check_id')}):
        #     check = qs.first()
        #     return (check.pdf_file, 'ok', 200) if check.status != 'new' else (None, 'Для данного чека не ' \
        #                                                                             'сгенерирован PDF-файл', 400)

        # for SQLite
        for check in qs:


            if {"id": kwargs.get('check_id')}.items() <= dict(check.order).items():  # проверяем совпадает ли id в
                # массиве, возвращаем чем если он готов(есть pdf - статус чека не new), или none - чек должен быть
                # один(уник), дальше смысла нет крутить цикл
                return (check.pdf_file, 'ok', 200) if check.status != 'new' else (None, 'Для данного чека не ' \
                                                                                        'сгенерирован PDF-файл', 400)
        return None, 'Данного чека не существует', 400
    else:
        return None, 'Не существует принтера с таким api_key', 401
