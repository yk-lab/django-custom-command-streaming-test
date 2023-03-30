from django.urls import path
from django.views.generic import TemplateView

from .apps import CoreConfig
from .views import non_stream_logs, stream_logs

app_name = CoreConfig.name

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='core/home.html'),
        name='home',
    ),
    path('stream_logs/', stream_logs, name='stream_logs'),
    path('non_stream_logs/', non_stream_logs, name='non_stream_logs'),
]
