
from django.contrib import admin
from django.urls import path
from api.views import RegisterAPI,StudentListCreateAPI,StudentRUD
#Login
from api.views import LoginAPI
from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', StudentListCreateAPI.as_view()),
    path('studentapi/<int:pk>/', StudentRUD.as_view()),
    path('studentapi/api/', RegisterAPI.as_view()),
    path('studentapi/login', LoginAPI.as_view()),


]
