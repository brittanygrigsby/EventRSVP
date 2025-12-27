from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from events.views import event_list
from rsvp.views import rsvp_home , home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('weddingrsvp/', rsvp_home, name='weddingrsvp'),
    path('events/', include('events.urls')),
    path('rsvp/', include('rsvp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
