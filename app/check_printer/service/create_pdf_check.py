import pdfkit
from django.template.loader import render_to_string
from django_rq import job

from check_printer.models import Check, CHECK_STATUS
from src.settings import MEDIA_ROOT


@job
def generate_pdf(obj: Check):
    """Generate PDF file"""
    # пропускаем данные через шаблон
    content = render_to_string(f'{obj.type}_check.html', obj.order)

    # создаем данные для отправки на конвертацию
    order_id = obj.order['id']
    check_type = obj.type
    name = f'{order_id}_{check_type}.pdf'
    path = MEDIA_ROOT / name
    pdfkit.from_string(content, path)  # конвертируем файл

    # Save link and status to db
    obj.status = CHECK_STATUS[1][0]
    obj.pdf_file = name
    obj.save()

