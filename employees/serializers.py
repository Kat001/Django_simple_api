from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		models = Course
		fields = ('id','name','language','price') 