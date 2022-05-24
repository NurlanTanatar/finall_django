from django.urls import path
from processing.views import BookAPIView, BookDetailApiView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view())
]
