"""djangoProjectKontRab7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from survey.views import Index, PollView, PollUpdate, PollDelete, PollCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/create/', PollCreate.as_view(), name="poll_create"),
    path('poll/<int:pk>/update', PollUpdate.as_view(), name="poll_update"),
    path('poll/<int:pk>/delete', PollDelete.as_view(), name="poll_delete"),
]
