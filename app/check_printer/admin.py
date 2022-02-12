from django.contrib import admin

# Register your models here.
from check_printer.models import Check, Printer


class CheckAdmin(admin.ModelAdmin):
    list_display = ['printer_id', 'type', 'order', 'status', 'pdf_file']
    list_filter = ['printer_id', 'type', 'status', ]


class TabChecks(admin.TabularInline):
    model = Check
    readonly_fields = ['printer_id', 'type', 'order', 'status', 'pdf_file']
    can_delete = False
    max_num = 0


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'check_type', 'point_id']
    list_filter = ['check_type', 'point_id']
    search_fields = ['api_key', 'name', ]
    search_help_text = 'search by name and apikey'
    inlines = [TabChecks, ]


admin.site.register(Check, CheckAdmin)
admin.site.register(Printer, PrinterAdmin)
