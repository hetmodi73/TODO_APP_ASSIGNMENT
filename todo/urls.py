from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewTaskView.as_view(),name="task-new"),
    path('view/',ListTaskView.as_view(),name="task-view"),
    path("update/<int:pk>",UpdateTaskView.as_view(),name="task-update"),
    path("delete/<int:pk>",DeleteTaskView.as_view(),name="task-delete"),
    path("detail/<int:pk>",DetailTaskView.as_view(),name="task-detail")
]
