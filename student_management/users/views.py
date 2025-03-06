from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, StudentProfileSerializer
from .models import StudentProfile
from .permissions import IsAdmin, IsTeacher,IsStudent

User = get_user_model()

# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Admin View
class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

# Teacher View
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='teacher')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsTeacher]

# Student View (Only Teachers Can Update Grades)
class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='student')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        - Teachers can view all students.
        - Students can only view their own data.
        """
        user = self.request.user
        if user.role == 'teacher':
            return User.objects.filter(role='student')  # Teacher sees all students
        return User.objects.filter(id=user.id)

    def update(self, request, *args, **kwargs):
        """Only teachers can update student grades"""
        student = self.get_object()

        if request.user.role != 'teacher':
            return Response({"error": "Only teachers can update grades."}, status=status.HTTP_403_FORBIDDEN)

        # Ensure StudentProfile exists
        try:
            student_profile = student.student_profile
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student profile not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update User including StudentProfile
        serializer = UserSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
