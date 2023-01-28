from django.urls import path
from . import views

urlpatterns = [
    path('', views.accept, name='form'),
    path('<int:id>/', views.cv, name='cv'),
    path('cv-list/', views.cv_list, name='cvlist')
]