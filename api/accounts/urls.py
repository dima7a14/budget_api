from rest_framework_nested import routers

from .views import AccountViewSet, TransactionViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="account")

account_router = routers.NestedDefaultRouter(router, r"accounts", lookup="account")
account_router.register(r"transactions", TransactionViewSet, basename="transaction")

category_router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    *router.urls,
    *account_router.urls,
    *category_router.urls,
]