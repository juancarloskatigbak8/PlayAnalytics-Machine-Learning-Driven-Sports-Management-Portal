from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('<int:player_id>/', views.player_detail, name='player_detail'),
    path('<int:player_id>/edit/', views.edit_player, name='edit_player'),
    path('<int:player_id>/add_journal/', views.add_journal_entry, name='add_journal'),
]
