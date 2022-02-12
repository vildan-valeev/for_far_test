import pdfkit
from django.template.loader import render_to_string
from django_rq import job

from check_printer.models import Check, CHECK_STATUS


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
    path = f'{order_id}_{check_type}.pdf'
    pdfkit.from_string(content, path)
    # with open(path, 'wb') as f:
    #     f.write(pdf)
    # Save link and status to db
    obj.status = CHECK_STATUS[1][0]
    obj.pdf_file = path
    obj.save()
