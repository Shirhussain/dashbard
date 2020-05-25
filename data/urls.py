from django.urls import path
from .views import create, listView, deleteView, updateView

app_name="data"
urlpatterns = [
    path('',create,name="create"),
    path('list',listView, name="listView"),
    path("<int:abc>/delete/", deleteView, name="delete"),
    path("<int:id>/update/", updateView, name="update")
]
