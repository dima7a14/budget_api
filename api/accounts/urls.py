from rest_framework_nested import routers

from .views import AccountViewSet, TransactionViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"categories", CategoryViewSet, basename="category")

# account_router = routers.NestedDefaultRouter(router, r"accounts", lookup="account")
# account_router.register(r"transactions", TransactionViewSet, basename="transaction")


urlpatterns = [
    *router.urls,
    # *account_router.urls,
]