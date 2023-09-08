from django.urls import path
from rest_framework import routers
from useraccount.api.viewsets import UserViewSet


router = routers.DefaultRouter()


router.register("useraccount", UserViewSet, basename="useraccount")



urlpatterns = router.urls