from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('snippet', views.SnippetViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]