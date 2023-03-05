# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import BlogsSerializer
from .models import BlogModel


# create a viewset
class BlogsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = BlogModel.objects.all()

    # specify serializer to be used
    serializer_class = BlogsSerializer
