from django.urls import path
from . import views
from .views import TestView

urlpatterns = [
    path(r'practice', TestView.as_view(), name='testview')
]
