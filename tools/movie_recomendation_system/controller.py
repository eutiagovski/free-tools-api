from flask import Response, request
from .model import MovieRecomendation


class MovieRecomendationController:
    def __init__(self):
        self.model=MovieRecomendation()

    def renderIndex(self):
        html = ''
        with open('/home/eutiagovski/mysite/tools/movie_recomendation_system/templates/index.html', encoding='utf-8') as f:
            for i in f:
                html += i
        html = html.encode('utf-8')
        return html

    def searchMovies(self):
        primaryTitle = str(request.args.get('title', ''))
        data = self.model.searchMovies(primaryTitle)
        # return {'status': True, 'data': [data], 'message': ''}
        return Response(data.to_json(orient="records"), mimetype='application/json')
    
    def getRecomendations(self):
        tconst = str(request.args.get('tconst', ''))
        data = self.model.getRecomendations(tconst)
        return Response(data.to_json(orient="records"), mimetype='application/json')
