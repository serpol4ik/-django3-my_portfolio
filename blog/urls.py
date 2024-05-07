from django.urls import path
from . import views


urlpatterns = [
    path('', views.last_blogs, name='last_blogs'),
    path('all', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]