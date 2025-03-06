from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import StudentProfile

User = get_user_model()

# Student Profile Serializer
class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['grade','attendance']

    def update(self, instance, validated_data):
        """Update the StudentProfile instance"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# User Serializer (Allow Updating student_profile)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    student_profile = StudentProfileSerializer(read_only=True)  # Allow updates

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'student_profile']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        student_profile_data = validated_data.pop('student_profile', None)

        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        if user.role == 'student' and student_profile_data:
            StudentProfile.objects.create(user=user, **student_profile_data)

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        student_profile_data = validated_data.pop('student_profile', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if student_profile_data and hasattr(instance, 'student_profile'):
            student_profile = instance.student_profile
            for attr, value in student_profile_data.items():
                setattr(student_profile, attr, value)
            student_profile.save()

        return instance
