from employees.models import Course
from rest_framework import serializers
from django.contrib.auth.models import User


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id','name','language','price')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'