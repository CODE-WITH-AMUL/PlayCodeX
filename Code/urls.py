from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# For the main programming lanaguage.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('direct/' , include('main.urls')),
    path('accounts/', include('loginprocess.urls')),
]
# for the programming laguage
apps_urlpatterns = [
    path('progarmming/', include('popularlanguage.urls')),
    
]
#connecting both url path
urlpatterns += apps_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)