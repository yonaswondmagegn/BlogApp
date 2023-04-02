from django.urls import path
from rest_framework_nested import routers 
from .views import ProfileViewset,BlogViewset

router = routers.DefaultRouter()
router.register('',ProfileViewset)

nested_routers = routers.NestedDefaultRouter(router,'',lookup = 'profile')
nested_routers.register('blogs',BlogViewset,basename='blogs')



urlpatterns = router.urls+nested_routers.urls