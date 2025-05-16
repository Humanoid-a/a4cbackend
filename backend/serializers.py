from rest_framework import serializers

from .models import School, FrontendUser, UserProfile
from decimal import Decimal


class UserProfileSerializer(serializers.ModelSerializer):
    nationality = serializers.CharField(source='nationality.code')
    class Meta:
        model = UserProfile
        # only expose read‑only fields if you don’t want clients to change these through this endpoint
        fields = [
            'sat_reading',
            'sat_math',
            'gpa',
            'intended_major',
            'recommendation_strength',
            'nationality',
            'gender',
        ]
        #read_only_fields = fields


class FrontendUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # nest the profile, read‑only
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = FrontendUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'biography',
            'profile_picture',
            'profile',             # ← include the nested profile
        ]

    def create(self, validated_data):
        # 1) Pop off the password
        password = validated_data.pop('password', None)

        # 2) Create the user
        user = FrontendUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        # 3) Create a default‐valued profile so the client doesn’t have to supply it
        UserProfile.objects.create(
            user=user,
            sat_reading=200,
            sat_math=200,
            gpa=Decimal('0.00'),  # Use Decimal for GPA
            recommendation_strength=1,
            # nationality can be left to its model default (blank=True, null=True)
            # or set explicitly if needed:
            # nationality=None, # or a default country code string like 'US'
        )

        return user

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

