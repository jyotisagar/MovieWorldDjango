from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/123
    path('<int:id>/', views.details, name='detail')
]
