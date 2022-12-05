from django.urls import path
from .views import SnackList, SnackDetail, SnackUpdate, SnackCreate, SnackDelete

urlpatterns = [
    # path('', HomePage.as_view(), name='home'),
    path("", SnackList.as_view(), name="SnackListView"),
    path("<int:pk>/", SnackDetail.as_view(), name="SnackDetailView"),
    path("create/", SnackCreate.as_view(), name="SnackCreateView"),
    path("<int:pk>/update/", SnackUpdate.as_view(), name="SnackUpdateView"),
    path("<int:pk>/delete/", SnackDelete.as_view(), name="SnackDeleteView"),
]
