"""
URL configuration for lal_injury_risk project.

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
from django.urls import path, include
from predictions.views import home, player_predictions, add_player, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('predictions/', player_predictions, name='player_predictions'),
    path('add_player/', add_player, name='add_player'),
    path('register/', register, name='register'),
    path('login/', include('django.contrib.auth.urls')),  # Built-in login/logout
]







