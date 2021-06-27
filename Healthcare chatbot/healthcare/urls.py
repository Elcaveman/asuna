from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
"""
    urls:
        api:
            /api/1.0.0/?
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
    #path('api/' , include('api.urls')),
    path('auth/' , include('user.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
