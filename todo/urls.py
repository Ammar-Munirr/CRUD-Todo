from django.urls import path
from . import views

urlpatterns = [
    path('task/',views.task,name='task'),
    path('task/delete/<int:id>',views.delete,name='delete')
]
