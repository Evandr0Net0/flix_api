from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres.')
        return value

    def validate_title(self, value):
        value = value.upper()

        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    # Campo além dos que já existem no model
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
    movies_by_genre = serializers.ListField()
