from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from imobiliaria.views import ImovelView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/imoveis/', ImovelView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
