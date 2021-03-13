from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('create',views.create,name="create"),
    path('show/<int:id>',views.show,name="show"),
    path('edit/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.update,name="delete")

]