from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
from application.models import Movie

class MovieList(ListView):
    model = Movie

class MovieView(DetailView):
    model = Movie

class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'description','rate']
    success_url = reverse_lazy('movie_list')

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name', 'description','rate']
    success_url = reverse_lazy('movie_list')

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')