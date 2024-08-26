from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  

from django.contrib import admin
from django.urls import path, include
from book_library import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Book-related URLs
    path('reviews/', include('reviews.urls')),  # Review-related URLs
    path('messages/', include('messaging.urls')),  # Messaging-related URLs
    path('accounts/', include('allauth.urls')),  # Authentication-related URLs (e.g., login, signup)
    path('users/', include('users.urls')),  # User-related URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)