from django.urls import path
from .views import BlogViewset,BlogCommentViewset,ProfileViewset
from rest_framework_nested import routers 

router = routers.DefaultRouter()
router.register('blogs',BlogViewset,basename='blog')

nested_routers = routers.NestedDefaultRouter(router,'blogs',lookup = 'blog')
nested_routers.register('comments',BlogCommentViewset,basename='comments')
nested_routers.register('author',ProfileViewset,basename='author')

urlpatterns = router.urls+nested_routers.urls