from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
