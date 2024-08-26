from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:book_pk>/review/', views.review_create, name='review_create'),
]