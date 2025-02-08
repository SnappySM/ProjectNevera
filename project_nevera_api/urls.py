from django.urls import include, path
from rest_framework import routers

from .views import user_view, refrigerator_view, food_view, item_view

router = routers.DefaultRouter()

router.register(r'users', user_view.UserViewset)
router.register(r'refrigerators', refrigerator_view.RefrigeratorViewset)
router.register(r'foods', food_view.FoodViewset)
router.register(r'items', item_view.ItemViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]