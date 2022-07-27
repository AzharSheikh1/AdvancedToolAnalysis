from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('data', views.HexDataViewSet, basename='hexdata')
router.register('hypo', views.HypothesisViewSet, basename='hypodata')
router.register('profile', views.ProfileViewSet)

urlpatterns = router.urls
