from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

base = settings.URLBASE
version = settings.APP_VERSION

urlpatterns = [
    # admin path
    path("admin/", admin.site.urls),
    # base urls
    path(f"{version}/{base}/base/", include("apps.base.urls")),
    # authentication
    path(f"{version}/{base}/auth/", include("apps.authentication.urls")),
    # expense_tracker app urls
    path(f"{version}/{base}/expense-tracker/", include("apps.expense_tracker.urls")),
    # swagger ui urls
    path(f"{version}/{base}/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"{version}/{base}/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
