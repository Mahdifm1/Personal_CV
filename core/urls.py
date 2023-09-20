from django.urls import path
from .views import index, download_cv

urlpatterns = [
    path('', index, name="index_page"),
    path('download-cv', download_cv, name="download_cv")
]
