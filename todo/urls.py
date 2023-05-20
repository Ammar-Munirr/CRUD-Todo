from django.urls import path
from . import views

urlpatterns = [
    path('task/',views.task,name='task'),
    path('task/delete/<int:id>',views.delete,name='delete'),
    path('task/edit/<int:id>',views.edit,name='Edit'),
    path('task/complete/<int:id>',views.complete,name='complete')
]
