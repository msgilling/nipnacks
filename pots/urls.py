from django.urls import path
from .views import PotDetailView, PotListView

urlpatterns = [
    path('', PotListView.as_view()),
    path('<int:pk>/', PotDetailView.as_view())
]