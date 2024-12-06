from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OmData
import pandas as pd
from django.utils.translation import gettext_lazy as translate  # Renamed for clarity
from django.urls import reverse  # Import reverse for URL redirection

@admin.register(OmData)
class OmDataAdmin(admin.ModelAdmin):
    change_list_template = 'om/omdata_changelist.html'

    list_display = [field.name for field in OmData._meta.fields]
    search_fields = ['Symbol', 'Company', 'Industry_Sector']
    list_per_page = 3000
    list_max_show_all = 3000
    actions = ['delete_selected_custom']

    def delete_selected_custom(self, request, queryset):
        # Warning message before deletion
        self.message_user(
            request,
            translate("Deleting selected records. This action cannot be undone."),
            level='warning'
        )

        # Proceed with deletion
        deleted_count, _ = queryset.delete()
        self.message_user(
            request,
            translate("Successfully deleted %(count)d records.") % {'count': deleted_count},
            level='success'
        )

    delete_selected_custom.short_description = "Delete selected records"

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
            try:
                # Load the uploaded Excel file into a DataFrame
                df = pd.read_excel(excel_file)

                # Check for action type
                if 'append' in request.POST:
                    # Append: Add data to the existing database
                    for _, row in df.iterrows():
                        OmData.objects.create(**row.to_dict())
                    self.message_user(request, "Data appended successfully.", level='success')

                elif 'replace' in request.POST:
                    # Replace: Clear existing data and insert new data
                    OmData.objects.all().delete()
                    for _, row in df.iterrows():
                        OmData.objects.create(**row.to_dict())
                    self.message_user(request, "Data replaced successfully.", level='success')

                # Redirect to the home page after successful upload
                return HttpResponseRedirect(reverse('home'))

            except Exception as e:
                # Handle errors and provide feedback
                self.message_user(
                    request,
                    f"An error occurred while processing the file: {str(e)}",
                    level='error'
                )
                return HttpResponseRedirect(request.path_info)

        # Render the upload form
        return render(request, 'om/upload.html')