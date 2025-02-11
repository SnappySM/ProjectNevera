from django.urls import include, path
from rest_framework import routers

from .views import user_view, refrigerator_view, food_view, item_view, key_term_view

router = routers.DefaultRouter()

router.register(r'users', user_view.UserViewset)
router.register(r'refrigerators', refrigerator_view.RefrigeratorViewset)
router.register(r'foods', food_view.FoodViewset)
router.register(r'items', item_view.ItemViewset)
router.register(r'keyterm', key_term_view.KeyTermViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]