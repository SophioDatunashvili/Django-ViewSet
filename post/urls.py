from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.PostViewSet, basename="post")

urlpatterns = router.urls
