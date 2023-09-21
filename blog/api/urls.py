from django.urls import path
from rest_framework import routers
from blog.api.viewsets import PostViewSet



app_name = "blog"


router = routers.DefaultRouter()


router.register("blog", PostViewSet, basename="blog")


urlpatterns = router.urls