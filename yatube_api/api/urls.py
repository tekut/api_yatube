from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from api.views import (UserViewSet,
                       PostViewSet,
                       GroupViewSet,
                       CommentViewSet,
                       )


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]


#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include(router.urls)),
#    path('api/', include(router.urls)),
#    path('auth/', include('djoser.urls')),
#    path('auth/', include('djoser.urls.jwt')),
#]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
