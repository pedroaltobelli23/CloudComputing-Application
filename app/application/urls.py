from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('view/<int:pk>', views.MovieView.as_view(), name='movie_view'),
    path('new', views.MovieCreate.as_view(), name='movie_new'),
    path('edit/<int:pk>', views.MovieUpdate.as_view(), name='movie_edit'),
    path('delete/<int:pk>', views.MovieDelete.as_view(), name='movie_delete'),
]