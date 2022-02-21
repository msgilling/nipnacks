from django.urls import path
from . import views
from .views import CommentListView
from .views import CommentDetailView

urlpatterns = [
    path('<int:pk>/', CommentDetailView.as_view()),
    path('', CommentListView.as_view()),
  ]