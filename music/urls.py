from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/1
    path('<int:id>/', views.details, name='detail'),

    # /music/1/favorite
    path('<int:id>/favorite', views.favorite, name='favorite')
]
