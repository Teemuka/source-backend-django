"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from main import views as main_views
from authentication import views as auth_views
from rest_framework import routers, serializers, viewsets



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'newstexts', main_views.NewsTextViewSet)
router.register(r'happenings', main_views.HappeningViewSet)
router.register(r'users', auth_views.UsersViewSet)


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns.append(url(r'^.*$', main_views.index, name='index'))
