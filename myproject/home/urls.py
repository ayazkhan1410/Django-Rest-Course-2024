from django.urls import path
from home import views
from .views import TodoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set', views.TodoViewSet, basename='todo')

urlpatterns = [
    
    # video tutorials
    path('', views.index, name='home'),
    path('post-todo/', views.post_todo, name='post-todo'),
    path('get-todo/', views.get_todo, name='get-todo'),
    path('todo-age/', views.todo_age, name='todo-age'),
    path('patch-todo/', views.patch_todo, name='patch-todo'),
    
    # my own practice 
    path('create-todo/', views.create_todo, name= 'create-todo'),
    path('update-todo/', views.update_todo, name = 'update-todo'),
    path('retrieves-data/', views.retrieves_data, name='retrieves-data'),
    path('partial-update/', views.partial_update, name='partial-update'),
    path('delete-data/', views.delete_data, name='delete-data'),
    
    # Class based views
    path('todo/', TodoView.as_view(), name='todo-list'),

]

urlpatterns += router.urls