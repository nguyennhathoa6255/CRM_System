from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('task/', include("tasks.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('crm.urls')),
#     path('task/', include("tasks.urls"))
# ]
