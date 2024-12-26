"""
URL configuration for withoutrest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.emp_data_view), # api
    path('apijson/', views.emp_data_jsonview, name='apijson'), #apijson
    path('apijson2/', views.emp_data_jsonview2, name='apijson2'), #apijson2
    path('apijsoncbv/', views.JsonCBV.as_view()),
]
