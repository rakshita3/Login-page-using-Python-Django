
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Signin.urls")),
    path('register',include("Signin.urls")),
    path('login',include("Signin.urls")),
]

urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)