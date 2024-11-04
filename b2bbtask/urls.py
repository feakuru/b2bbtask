from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from wallet import views as wallet_views

router = routers.DefaultRouter()
router.register(r"wallets", wallet_views.WalletViewSet)
router.register(r"transactions", wallet_views.TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
