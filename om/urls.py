

from django.urls import path
from . import views
from django.urls import path
from django.urls import path
from .views import om_data_letter_grades_view, download_pdf
from django.conf.urls.static import static
from django.conf import settings
from .views import deep_dive_view
from .views import update_record
from .views import delete_record
from .views import manage_records

urlpatterns = [
    path('data/', views.om_data_list, name='data_list'),  # List of data
    path('upload/', views.upload_om_data, name='upload_data'),  # Upload data
    path('download/', views.download_excel, name='download_excel'),  # Download route
    path('', views.om_data_list, name='home'),  # Point root URL to om_data_list
    path('letter-grades/', om_data_letter_grades_view, name='letter_grades'),  # Letter grades view
    path('TheOddsMaker/', views.om_data_TheOddsMaker_view, name='TheOddsMaker'),  # Odds Maker view
    path('deep-dive/', deep_dive_view, name='deep_dive'),  # Deep dive view
    path('manage/', manage_records, name='manage_records'),  # Manage records view
    path('update_record/<int:record_id>/', update_record, name='update_record'),  # Update record route
    path('delete_record/<int:id>/', views.delete_record, name='delete_record')
]

if settings.DEBUG:  # Only serve files this way in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)