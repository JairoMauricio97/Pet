from django.urls import path
from pet import views

urlpatterns = [
path('', views.Blog, name='Blog'),
path('<int:pk>/', views.perritoDetalle, name='perritoDetalle'),
]