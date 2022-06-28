from Watchmate.models import Movie
# from rest_framework.decorators import api_view
from rest_framework import status
from Watchmate.API.serializer import Movie_Serializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = Movie_Serializer(movies, many = True)
        content = {'please go to home page' : 'Please find all Movies details here '}
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Movie_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'please go to home page' : 'Movie details has been created successfully'}
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            content = {'try agin' : 'invalid details please check it!'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)   
        
        
class MovieDetailsView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            content = {'please go to home page' : 'Movie id not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND) 
        else:
            serializer = Movie_Serializer(movie)
            content = {'please go to home page' : 'Please movie details here'}
            return Response( serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            content = {'please go to home page' : 'Movie id not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND) 
        else:   
            serializer = Movie_Serializer(movie, data=request.data) 
            if serializer.is_valid():
                serializer.save()
                    
                content = {'please go to home page' : 'Movie details has been updated successfully'}
                return Response( serializer.data, status=status.HTTP_201_CREATED)  
            else:
                content = {'try agin' : 'invalid details please check it!'}
                return Response(content, status=status.HTTP_404_NOT_FOUND) 
    
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            content = {'please go to home page' : 'Movie id not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND) 
        else:    
            movie.delete()
            content = {'please go to home page' : 'Movie details has been deleted successfully'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        
                
            
        











# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = Movie_Serializer(movies, many = True)
        
#         content = {'please go to home page' : 'Please find all Movies details here '}
#         return Response(serializer.data, status=status.HTTP_200_OK) 
    
#     if request.method == 'POST':
#         serializer = Movie_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             content = {'please go to home page' : 'Movie details has been created successfully'}
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         else:
           
#             content = {'try agin' : 'invalid details please check it!'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND)   


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, movie_id):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             content = {'please go to home page' : 'Movie id not found'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND) 
#         else:
#             serializer = Movie_Serializer(movie)
#             content = {'please go to home page' : 'Please movie details here'}
#             return Response( serializer.data, status=status.HTTP_200_OK) 
    
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             content = {'please go to home page' : 'Movie id not found'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND) 
#         else:   
#             serializer = Movie_Serializer(movie, data=request.data) 
#             if serializer.is_valid():
#                 serializer.save()
                    
#                 content = {'please go to home page' : 'Movie details has been updated successfully'}
#                 return Response( serializer.data, status=status.HTTP_201_CREATED)  
#             else:
#                 content = {'try agin' : 'invalid details please check it!'}
#                 return Response(content, status=status.HTTP_404_NOT_FOUND) 
        
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             content = {'please go to home page' : 'Movie id not found'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND) 
#         else:    
#             movie.delete()
#             content = {'please go to home page' : 'Movie details has been deleted successfully'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND)
    