from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('election_portal/', include('geolocation.urls')),
	path('election_portal/', include('voter.urls')),
	path('election_portal/admin/', admin.site.urls),
    path('election_portal/oauth2/', include('django_auth_adfs.urls')),
	path('election_portal/', include('results.urls')),
	path('election_portal/results/progress',include('celery_progress.urls')),
	path('election/', include('stats.urls')),
	path('election/', include("preelection.urls")), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
# 	urlpatterns+=static(settings.STATIC_URL)
