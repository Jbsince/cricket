
from django.urls import path, include
from . import views
app_name='cricketapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/<int:profile_id>/',views.details,name='details'),
    path('add/',views.add_player,name='add_player'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
