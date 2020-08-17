from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name='home'),
    path('create_task/', views.add_task, name='create_task'),
    path('done_tasks/', views.done_tasks, name='done_tasks'),

    path('login/', views.loginView , name='login'),
    path('register/', views.registerView , name='register'),
    path('logout/', views.logoutview , name='logout'),
    
    path('add_done/<str:pk>', views.add_done_tasks , name='add_done'),
    path('update_task/<str:pk>', views.updateTask , name='update_task'),
    path('delete_task/<str:pk>' , views.deleteTask , name='delete_task')

    
]


