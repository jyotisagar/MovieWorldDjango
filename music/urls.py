from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/1
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]
