"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_user,name='login'),
    path('register/',views.reg_user,name='reg_user')
    path('site/',views.view_detail,name='view_detail')
    path('view_detail_db/',views.view_detail_db,name='view_detail_db')
    
]
