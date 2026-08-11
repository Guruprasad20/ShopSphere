from django.urls import path
from .views import dashboard, api_docs
urlpatterns=[path("",dashboard,name="dashboard"),path("api-docs/",api_docs,name="api_docs")]
