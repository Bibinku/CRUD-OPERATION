from django.urls import path
from Movieapp import views


urlpatterns = [
    path('',views.Function,name="Function"),
    path('save/', views.save_data, name="save_data"),
    path('display/', views.display, name="display"),
    path('edit/<int:Nameid>/', views.editdisplay, name="editdisplay"),

]
