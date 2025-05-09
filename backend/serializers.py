from rest_framework import serializers

from .models import School, FrontendUser, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
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
        read_only_fields = fields


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
            sat_reading=200,            # lowest valid SAT reading
            sat_math=200,               # lowest valid SAT math
            gpa=0.00,                   # lowest valid GPA
            # `intended_major` and `gender` have defaults on the model,
            # so you can omit them here if you like:
            recommendation_strength=1,  # minimum allowed rec strength
            nationality='',             # blank country; change as you see fit
        )

        return user

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

