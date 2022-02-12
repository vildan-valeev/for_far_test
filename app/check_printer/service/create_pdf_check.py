import os

import pdfkit
from django.template.loader import render_to_string
from django_rq import job

from check_printer.models import Check, CHECK_STATUS
from src.settings import MEDIA_ROOT, BASE_DIR


@job
def generate_pdf(obj: Check):
    print(f'Запущена фоновая задача! создаем пдф файлы для  {obj.printer_id.name}')
    # time.sleep(5)

    # пропускаем данные через шаблон
    content = render_to_string(f'{obj.type}_check.html', obj.order)
    # print(content)
    # data = {'contents': open('/file/to/convert.html').read().encode('base64'),}

    # создаем данные для отправки на конвертацию


    # Save the response contents to a file
    order_id = obj.order['id']
    check_type = obj.type
    name = f'{order_id}_{check_type}.pdf'
    path = MEDIA_ROOT / name
    print(path)
    pdfkit.from_string(content, path)

    # Save link and status to db
    obj.status = CHECK_STATUS[1][0]
    obj.pdf_file = name
    obj.save()
