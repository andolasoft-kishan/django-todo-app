from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_todo, name='add'),
    path('list/', list, name='list'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('signup/', signup, name='signup'),
    path('complete/<int:pk>/', complete_todo, name='complete'),
    path('api/', include(router.urls)),
]
