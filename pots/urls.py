from django.urls import path
from .views import PotListView

urlpatterns = [
  path('', PotListView.as_view())
]