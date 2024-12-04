from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OmData
import pandas as pd
from django.utils.translation import gettext_lazy as _

@admin.register(OmData)
class OmDataAdmin(admin.ModelAdmin):
    change_list_template = 'om/omdata_changelist.html'  # Specify your custom template

    list_display = [field.name for field in OmData._meta.fields]
    search_fields = ['Symbol', 'Company', 'Industry_Sector']
    list_per_page = 3000
    list_max_show_all = 3000
    actions = ['delete_selected_custom']

    def delete_selected_custom(self, request, queryset):
        if queryset.count() > 10000:
            self.message_user(
                request,
                _("You can only delete up to 10,000 records at a time."),
                level='error'
            )
            return

        deleted_count, _ = queryset.delete()
        self.message_user(
            request,
            _("Successfully deleted %(count)d records.") % {'count': deleted_count},
            level='success'
        )

    delete_selected_custom.short_description = "Delete selected records (up to 10,000)"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download/', self.admin_site.admin_view(self.download_excel), name='download_excel'),
            path('upload/', self.admin_site.admin_view(self.upload_om_data), name='upload_data'),
        ]
        return custom_urls + urls

    def download_excel(self, request):
        data = OmData.objects.all().values()
        if data.exists():
            df = pd.DataFrame(data)
        else:
            field_names = [field.name for field in OmData._meta.fields]
            df = pd.DataFrame(columns=field_names)

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="om_data.xlsx"'
        df.to_excel(response, index=False)
        return response

    def upload_om_data(self, request):
        if request.method == 'POST' and request.FILES.get('excel_file'):
            excel_file = request.FILES['excel_file']
            # Process the uploaded file
            df = pd.read_excel(excel_file)

            # Implement your logic for appending or replacing data
            # Example:
            # if 'append' in request.POST:
            #     # Logic to append data
            # elif 'replace' in request.POST:
            #     # Logic to replace data

            self.message_user(request, "Data uploaded successfully.")
            return HttpResponseRedirect(request.path_info)  # Redirect to the same page after upload

        return render(request, 'om/upload.html')  # Render the upload template