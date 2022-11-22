from django.contrib import admin
from django.urls import path
from . import views #from . - означает, что импорт из этой же директории

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.myhome),
    path('reverse/', views.reverse, name= 'reversed')
]
