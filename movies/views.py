from django.db.models import Avg
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailSerializer
from reviews.models import Review
from django.db.models import Count


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer

        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer

        return MovieModelSerializer


class MovieStatsView(views.APIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):

        return response.Response(
            data={'message': 'Funcionou'},
            status=status.HTTP_200_OK,
        )
