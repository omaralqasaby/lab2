from django.urls import path
from .views import index,create,MovieList,MovieCreate,MovieUpdate


urlpatterns=[
    path('',index),
    path('create',create),
    path('list/',MovieList.as_view()),
    path('create/',MovieCreate.as_view()),
    path('update/<int:pk>/',MovieUpdate.as_view())
]