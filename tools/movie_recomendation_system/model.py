import pandas as pd
import joblib
import sys

print(sys.path)
movies, cousine_sim = joblib.load('./tools/movie_recomendation_system/ai_models/model_v1.joblib')


class MovieRecomendation:
    def __init__(self):
        self.movies = movies
        self.cousine_sim = cousine_sim

    def searchMovies(self, primaryTitle):
        movies = self.movies
        movies = movies.loc[movies.primaryTitle_ptBr.str.lower().str.contains(primaryTitle)]
        movies =  movies.sort_values('startYear', ascending=False)
        return movies
    
    def getRecomendations(self, tconst):
        # reset movies index
        movies = self.movies
        movies.reset_index(drop=True, inplace=True)

        # find the index for the given movie
        indices = pd.Series(movies.index, index=movies['tconst'])
        idx = indices[tconst]

        # filter similar titles
        sim_scores = list(enumerate(self.cousine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:11]

        movie_indices = [i[0] for i in sim_scores]

        movies = movies.iloc[movie_indices].sort_values('startYear', ascending=False)
        return movies