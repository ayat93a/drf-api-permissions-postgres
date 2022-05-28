from rest_framework.generics import ( ListCreateAPIView,
                                      RetrieveUpdateDestroyAPIView,
                                                        )
from movies.models import Movie
from .serializers import Movieserializers
from .permissions import IsAuthorOrReadOnly


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movieserializers

class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movieserializers
    permission_classes = (IsAuthorOrReadOnly,)