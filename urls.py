from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('home/', view_home),
    path('show/', view_show),
    path('dtl/', view_dtl),
    path('costumer/', cms_view),
    path('Employee/', view_Emp)


]
