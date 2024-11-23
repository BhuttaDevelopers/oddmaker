

from django.urls import path
from . import views
from django.urls import path
from django.urls import path
from .views import om_data_letter_grades_view, download_pdf
from django.conf.urls.static import static
from django.conf import settings
from .views import deep_dive_view  

urlpatterns = [
    path('data/', views.om_data_list, name='data_list'),
    path('upload/', views.upload_om_data, name='upload_data'),
    path('download/', views.download_excel, name='download_excel'),  # Download route
    path('', views.om_data_list, name='home'),  # Point root URL to om_data_list
    path('letter-grades/', views.om_data_letter_grades_view, name='letter_grades'),  # Letter grades view
    path('TheOddsMaker/', views.om_data_TheOddsMaker_view, name='TheOddsMaker'),  # Letter grades view
    path('download_pdf/', download_pdf, name='download_pdf'),  # Add this line TheOddsmaker_view
    path('deep-dive/', deep_dive_view, name='deep_dive'),  # Add this line
]

if settings.DEBUG:  # Only serve files this way in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)