from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework_extensions.routers import ExtendedDefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import AuthorViewSet, BookViewSet

router = ExtendedDefaultRouter()
(
    router.register('author', AuthorViewSet)
    .register('books', BookViewSet, basename='author-books',
              parents_query_lookups=['authors__slug', ])
)
router.register('book', BookViewSet)

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
        ),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
        ),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls))
]
