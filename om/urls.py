

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
from .views import upload_om_data, download_excel  # Import your views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('data/', views.om_data_list, name='data_list'),  # List of data
    path('upside/', views.om_upside, name='upside'),  # List of data
     path('10upside/', views.om_10upside, name='10upside'),  # List of data 
    path('upload/', views.upload_om_data, name='upload_data'),  # Upload data
    path('download/', views.download_excel, name='download_excel'),  # Download route
    path('', views.om_data_list, name='home'),  # Point root URL to om_data_list
    path('letter-grades/', om_data_letter_grades_view, name='letter_grades'),  # Letter grades view
    path('TheOddsMaker/', views.om_data_TheOddsMaker_view, name='TheOddsMaker'),  # Odds Maker view
    path('deep-dive/', deep_dive_view, name='deep_dive'),  # Deep dive view
    path('manage/', views.manage_records, name='manage_records'),
    path('upload/', views.upload_om_data, name='upload_om_data'),
    path('download/', views.download_excel, name='download_om_data'),
    path('update_record/<int:record_id>/', views.update_record, name='update_record'),
    path('delete_record/<int:id>/', views.delete_record, name='delete_record'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
]

if settings.DEBUG:  # Only serve files this way in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)