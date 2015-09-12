from django.conf.urls import url
from coming_soon.views import ComingSoon

urlpatterns = [
    url(r'', ComingSoon.as_view(), name="soon"),
]
