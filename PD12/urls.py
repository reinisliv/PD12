"""PD12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.UserListView.as_view(), name='user-list'),
    path('add_user', user.views.AddUserView.as_view()),
    path('get_user/<int:user_id>', user.views.GetUserView.as_view()),
    path('edit_user/<int:user_id>', user.views.EditUserView.as_view()),
    path('delete_user/<int:user_id>', user.views.DeleteUserView.as_view()),
]
