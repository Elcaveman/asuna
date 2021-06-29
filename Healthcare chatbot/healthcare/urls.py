from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
"""
    urls:
        api:
            /api/v1/interviews/
            /api/v1/diseases/
        auth:
            /auth/login
            /auth/logout
            /auth/profil
                -> if profile new redirect ( profil/new )
        base:
            /about
            /chat  -> chatbot
            /      -> homepage
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('base.urls')),
    path('api/v1/' , include('api.urls')),
    path('auth/' , include('user.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
