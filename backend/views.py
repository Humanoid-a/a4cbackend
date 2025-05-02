from rest_framework import viewsets
from .models import School
from .serializers import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('-school_id')
    serializer_class = SchoolSerializer
