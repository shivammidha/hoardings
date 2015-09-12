from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('coming_soon.urls', namespace="coming_soon")),
]
