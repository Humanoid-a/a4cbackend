from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .models import School, FrontendUser, UserProfile
from .serializers import (
    SchoolSerializer,
    FrontendUserSerializer,
    UserProfileSerializer,
)

class RegisterView(CreateAPIView):
    queryset = FrontendUser.objects.all()
    serializer_class = FrontendUserSerializer
    permission_classes = [permissions.AllowAny]

class FrontendUserViewSet(viewsets.ModelViewSet):
    queryset = FrontendUser.objects.all()
    serializer_class = FrontendUserSerializer

    # only allow authenticated users to edit their own data:
    permission_classes = [permissions.IsAuthenticated]


class ProfileView(RetrieveUpdateAPIView):
    """
    GET  /api/profile/     → returns the logged-in user’s profile
    PUT  /api/profile/     → replaces it
    PATCH/POST /api/profile/ → partial updates
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # assumes you have a OneToOne from FrontendUser → UserProfile named 'profile'
        if self.request.user.profile == None:
            profile, created = UserProfile.objects.get_or_create(
                user=self.request.user,
                defaults={
                    'sat_reading': 200,
                    'sat_math': 200,
                    'gpa': 0.00,
                    'recommendation_strength': 1,
                    'nationality': '',  # make sure your model allows blank=''
                    # intended_major and gender will use their model defaults
                }
            )
            self.request.user.profile = profile
        return self.request.user.profile

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('school_id')
    serializer_class = SchoolSerializer
