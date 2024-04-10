from flask import Blueprint
from .controller import MovieRecomendationController

movie_recomendation=Blueprint('movie_recomendation', __name__, url_prefix='/movie-recomendation-system')

@movie_recomendation.get('/')
def index():
    return MovieRecomendationController().renderIndex()

@movie_recomendation.get('/api/search-movie')
def searchMovie():
    return MovieRecomendationController().searchMovies()

@movie_recomendation.get('/api/recomend-movies')
def getRecomendations():
    return MovieRecomendationController().getRecomendations()