from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-control-panel/', admin.site.urls),
    path('',include('main.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "VCET HACKATHON 2021"
admin.site.site_title = "VCET HACKATHON 2021"
admin.site.index_title = ""