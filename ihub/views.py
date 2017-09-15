from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ihub.models import Student
# Create your views here.
# Serializers define the API representation.
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('names', 'course', 'description', 'registration_date','graduation_date')

# ViewSets define the view behavior.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer