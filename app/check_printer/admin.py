from django.contrib import admin

# Register your models here.
from check_printer.models import Check, Printer


class CheckAdmin(admin.ModelAdmin):
    list_display = ['printer_id', 'type', 'order', 'status', 'pdf_file']
    list_filter = ['printer_id', 'type', 'status', ]


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'check_type', 'point_id']
    list_filter = ['check_type', 'point_id']


admin.site.register(Check, CheckAdmin)
admin.site.register(Printer, PrinterAdmin)