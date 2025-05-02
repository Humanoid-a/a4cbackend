from rest_framework import viewsets, permissions

from .models import School
from .serializers import SchoolSerializer
from .models import FrontendUser
from .serializers import FrontendUserSerializer

class FrontendUserViewSet(viewsets.ModelViewSet):
    queryset = FrontendUser.objects.all().order_by('username')
    serializer_class = FrontendUserSerializer
    permission_classes = [permissions.AllowAny]  # or restrict as you see fit


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('school_id')
    serializer_class = SchoolSerializer
