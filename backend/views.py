from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView

from .models import School
from .serializers import SchoolSerializer
from .models import FrontendUser
from .serializers import FrontendUserSerializer

class RegisterView(CreateAPIView):
    queryset = FrontendUser.objects.all()
    serializer_class = FrontendUserSerializer
    permission_classes = [permissions.AllowAny]


class FrontendUserViewSet(viewsets.ModelViewSet):
    queryset = FrontendUser.objects.all()
    serializer_class = FrontendUserSerializer

    # only allow authenticated users to edit their own data:
    permission_classes = [permissions.IsAuthenticated]


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('school_id')
    serializer_class = SchoolSerializer
