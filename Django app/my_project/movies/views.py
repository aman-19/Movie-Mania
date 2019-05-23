from django.shortcuts import render
from rest_framework import generics
from .models import Cast_List,Movies_list
from .serializers import Movies_list_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MovieListView(generics.ListCreateAPIView):
    queryset = Movies_list.objects.all()
    serializer_class = Movies_list_Serializer



class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movies_list.objects.all()
    serializer_class = Movies_list_Serializer

import heapq
import my_project.settings
from .get_autocomplete import Query
class Auto_complete_View(APIView):
    def get(self,request):
        prefix = (request.GET.get('prefix'))
        try:
            limit = int(request.GET.get('limit'))
        except:
            limit = 5 # default value
        try:
            offset = int(request.GET.get('offset'))
        except:
            offset = 0 # default value

        new_query = Query()

        # getting list of movies closely matching with prefix
        matched = new_query.search(my_project.settings.Trie, prefix, limit+offset)
        
        result = []

        # extracting info from list of tuples
        while len(matched) > 0:
            result.append({'Movie Name':matched[0][2], 'MovieId':matched[0][1], 'Rating':matched[0][0]})
            heapq.heappop(matched)

        # if movies are more than offset then provide movies after offset
        if len(result) > offset:
            while offset > 0:
                result.pop()
                offset -= 1

        # descending order according to the rating of movies
        result.reverse()
        return Response(result)


# no use to create trie again and again unless and until database is updated

from .trie import make_Trie
if len(my_project.settings.Trie) == 0:
    data = Movies_list.objects.all()
    make_Trie(data, my_project.settings.Trie)


# use only when database is to be created

# import my_project.settings
# if my_project.settings.DatabaseToCreate:
#     from .loadMovies import saveMovies
#     saveMovies()
#     my_project.settings.DatabaseToCreate = False
