from django.urls import path
from . views import company_article
app_name="finance"
urlpatterns = [
    path("companies/",company_article, name="companies")
]