from django.urls import path
from adminportfolio.api.views import ProjectItemList

urlpatterns = [
    path("adminportfolio/", ProjectItemList.as_view(), name="project-list")
]
