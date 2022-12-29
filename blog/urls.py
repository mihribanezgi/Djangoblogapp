"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from article import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
     path("", views.index, name="index"),
     path("about/", views.about, name="about"),
     path("detail/<int:id>", views.detail, name="detail"), #dinamik url adresi tanımladım localhost:8000/detail/1
     path('articles/',include("article.urls")), #articles gördükten sonra sen git oluşturduğum articledaki urls.py'e bak localhostta /articles/create dersek bu çalışacak 
     path("user/",include("user.urls")), #localhost:8000/user/register gibi  oluşturduğum app uygulamasındaki urls.py'e gider ve o urlsi çalıştırır

     
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
