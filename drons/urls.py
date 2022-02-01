from django.urls import path
from rest_framework.routers import SimpleRouter

from drons import views

app_name = 'drones'

# router = SimpleRouter()
# router.register('drones-categories', views.DroneCategoryViewSet, basename='drone-categories')
# router.register('drones', views.DroneViewSet, basename='drones')
# router.register('pilots', views.PilotViewSet, basename='pilots')
# router.register('competitions', views.CompetitionViewSet, basename='competitions')

# urlpatterns = router.urls
urlpatterns = [
    path('drones/', views.DroneList.as_view(), name='drones'),
    path('drones/<int:pk>/', views.DroneDetail.as_view(), name='drones-detail'),
    path('competitions/', views.CompetitionList.as_view(), name='competitions'),
    path('competitions/<int:pk>/', views.CompetitionDetail.as_view(), name='competitions-detail')
]