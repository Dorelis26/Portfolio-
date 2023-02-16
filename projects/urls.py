
from . import views
from django.urls import path

app_name = 'projects'
urlpatterns = [
    path('',views.all_projects,name='home'),
    path('<int:pk>/', views.project_detail,name='detail')
]
