from django.urls import path
from Movieapp import views


urlpatterns = [
    path('',views.Function,name="Function"),
]
