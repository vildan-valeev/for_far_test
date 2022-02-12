from typing import Tuple

from check_printer.models import Printer, Check
from check_printer.service.create_pdf_check import generate_pdf


def create_checks(data: dict) -> Tuple[bool, str]:
    """Создание чека в бд"""
    message = 'Чеки успешно созданы'
    printers = Printer.objects.filter(point_id=data['point_id'])
    if printers.exists():  # есть ли принтеры
        for p in printers:  # создаем чек для каждого принтера
            print('CREATING', p.check_type, p.name, data)
            obj, created = Check.objects.get_or_create(printer_id=p, order=data, type=p.check_type)
            if not created:  # если такой json уже приходил
                return False, 'Для данного заказа уже созданы чеки'
            # generate_pdf.delay(obj)
            generate_pdf(obj)
    else:
        return False, 'Для данной точки не настроено ни одного принтера'
    return True, message
